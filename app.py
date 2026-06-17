from flask import Flask, jsonify, request, render_template
from duties import handle_create_duty
from services.coin_service import CoinService
from services.duty_service import DutyService

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

    response = {
        "success": created_coin["success"],
        "data": {
            "id": str(created_coin["data"].id),
            "name": created_coin["data"].name,
            "is_complete": created_coin["data"].is_complete
        },
        "error": created_coin["error"]
    }

    return jsonify(response), 201

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)