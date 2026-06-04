from flask import Flask, jsonify, request, render_template
from duties import handle_create_duty
from services.coin_service import CoinService
from services.duty_service import DutyService

app = Flask(__name__)

service = DutyService()
coin_service = CoinService()

app.service = service
app.coin_service = coin_service

@app.route("/", methods=["GET", "POST"])
def home():

    error = None

    if request.method == "POST":
        number = request.form.get("number")
        description = request.form.get("description")

        result = handle_create_duty(number, description, service.duties)

        if result["success"]:
            service.duties.append(result["duty"])
            error = None
        else:
            error = result["error"]

    return render_template(
        "index.html",
        duties=service.duties,
        error=error
    )

@app.route("/coins", methods=["GET"])
def get_coins():
    return jsonify([])

@app.route("/coins/<coin_id>", methods=["GET"])
def get_coin_by_id(coin_id):
    for coin in app.coin_service.coins:
        if coin.id == coin_id:
            return jsonify({
                "id": coin.id,
                "name": coin.name
            }), 200
    
    return None
    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
