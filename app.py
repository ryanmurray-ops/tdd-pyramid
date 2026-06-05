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
        number = request.form.get("number")
        description = request.form.get("description")

        result = handle_create_duty(number, description, duty_service.duties)

        if result["success"]:
            duty_service.duties.append(result["duty"])
            error = None
        else:
            error = result["error"]

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
    coin_data = request.get_json()
    coin = coin_service.create_coin(coin_data["name"])
    return {
        "id": coin.id,
        "name": coin.name
    }, 201

@app.route("/coins/<coin_id>", methods=["GET"])
def get_coin_by_id(coin_id):
    for coin in app.coin_service.coins:
        if coin.id == coin_id:
            return jsonify({
                "id": coin.id,
                "name": coin.name
            }), 200
    
    return jsonify({"error": "Coin not found"}), 404

@app.route("/coins/<coin_id>", methods=["PUT"])
def update_coin(coin_id):
    coin_update_request = request.get_json()

    for coin in app.coin_service.coins:
        if coin.id == coin_id:
            coin.is_complete = coin_update_request["is_complete"]
            return {}, 200

    return {"error": "Coin not found"}, 404

@app.route("/coins/<coin_id>", methods=["DELETE"])
def delete_coin(coin_id):
    for coin in app.coin_service.coins:
        if coin.id == coin_id:
            app.coin_service.coins.remove(coin)
            return {}, 200
    return {}, 404
    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
