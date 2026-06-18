from flask import Flask, jsonify, request, render_template
from duties import handle_create_duty
from services.coin_service import CoinService
from services.duty_service import DutyService
from utils.coin_mapper import format_coin_list, format_coin_response

app = Flask(__name__)

app.duty_service = DutyService()
app.coin_service = CoinService()

@app.route("/", methods=["GET", "POST"])
def home():

    error = None

    if request.method == "POST":
        number = request.form.get("number")
        description = request.form.get("description")

        result = handle_create_duty(number, description, app.duty_service.duties)

        if result["success"]:
            app.duty_service.duties.append(result["duty"])
            error = None
        else:
            error = result["error"]

    return render_template(
        "index.html",
        duties=app.duty_service.duties,
        error=error
    )

@app.route("/coins", methods=["POST"])
def create_coin():
    create_coin_request = request.get_json()

    created_coin = app.coin_service.create_coin(create_coin_request["name"])

    if not created_coin["success"]:
        return jsonify(created_coin), 400

    return jsonify(format_coin_response(created_coin)), 201

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

@app.route("/coins", methods=["GET"])
def get_coins():
    coins_response = app.coin_service.get_all_coins()

    return jsonify({
        "success": True,
        "data": format_coin_list(coins_response["data"]),
        "error": None
    }), 200

@app.route("/coins/<coin_id>", methods=["GET"])
def get_coin_by_id(coin_id):
    coin_response = app.coin_service.get_coin_by_id(coin_id)

    if not coin_response["success"]:
        return jsonify(coin_response), 404

    return jsonify(format_coin_response(coin_response)), 200

@app.route("/coins/<coin_id>", methods=["DELETE"])
def delete_coin(coin_id):
    delete_response = app.coin_service.delete_coin(coin_id)

    if not delete_response["success"]:
        return jsonify(delete_response), 404

    return jsonify(delete_response), 200

@app.route("/coins/<coin_id>", methods=["PUT"])
def update_coin(coin_id):
    request_data = request.get_json()

    update_response = app.coin_service.update_coin(coin_id, request_data["name"])

    if not update_response["success"]:

        if update_response["error"] == "Coin not found":
            return jsonify(update_response), 404
        
        if update_response["error"] == "Coin already exists":
            return jsonify(update_response), 400

    return jsonify(format_coin_response(update_response)), 200

