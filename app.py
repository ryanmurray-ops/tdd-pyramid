from flask import Flask, jsonify, request, render_template
from duties import handle_create_duty
from services.coin_service import CoinService
from services.duty_service import DutyService

app = Flask(__name__)

duty_service = DutyService()
coin_service = CoinService()

app.duty_service = duty_service
app.coin_service = coin_service

@app.route("/", methods=["GET", "POST"])
def home():

    error = None

    if request.method == "POST":
        duty_form_data = request.form

        create_duty_result = handle_create_duty(
            duty_form_data.get("number"),
            duty_form_data.get("description"),
            duty_service.duties
        )

        if create_duty_result["success"]:
            duty_service.duties.append(create_duty_result["duty"])
            error = None
        else:
            error = create_duty_result["error"]

    return render_template(
        "index.html",
        duties=duty_service.duties,
        error=error
    )

@app.route("/coins", methods=["GET"])
def get_coins():
    return jsonify([])

@app.route("/coins", methods=["POST"])
def create_coin():
    coin_creation_data = request.get_json()
    new_coin = coin_service.create_coin(coin_creation_data["name"])
    return {
        "id": new_coin.id,
        "name": new_coin.name
    }, 201

@app.route("/coins/<coin_id>", methods=["GET"])
def get_coin_by_id(coin_id):
    coin = app.coin_service.get_coin_by_id(coin_id)

    if coin:
        return jsonify({
            "id": coin.id,
            "name": coin.name
        }), 200

    return jsonify({"error": "Coin not found"}), 404

@app.route("/coins/<coin_id>", methods=["PUT"])
def update_coin(coin_id):
    update_coin_data = request.get_json()
    updated_coin = app.coin_service.update_coin(
        coin_id,
        update_coin_data["is_complete"]
    )

    if updated_coin:
        return {}, 200
    
    return {"error": "Coin not found"}, 404

@app.route("/coins/<coin_id>", methods=["DELETE"])
def delete_coin(coin_id):
    coin_deleted = app.coin_service.delete_coin(coin_id)

    if coin_deleted:
        return {}, 200
    return {"error": "Coin not found"}, 404
    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
