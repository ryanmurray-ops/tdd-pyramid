from flask import Flask, jsonify, request, render_template
from database import init_db
from services.coin_service import CoinService
from services.duty_service import DutyService
from services.repositories.database_coin_repository import DatabaseCoinRepository
from services.repositories.database_duty_repository import DatabaseDutyRepository
from services.repositories.in_memory_coin_repository import InMemoryCoinRepository
from services.repositories.in_memory_duty_repository import InMemoryDutyRepository
from validators import validate_duty_request

def create_app(coin_repository, duty_repository):
    app = Flask(__name__)
    init_db()

    # -----------------------
    # Services
    # -----------------------

    app.coin_service = CoinService(coin_repository)
    app.duty_service = DutyService(duty_repository)



    # -----------------------
    # Home route (duties)
    # -----------------------

    @app.route("/", methods=["GET", "POST"])
    def home():
        error = None

        if request.method == "POST":
            number = (request.form.get("number") or "").strip()
            description = (request.form.get("description") or ""). strip()

            if not number and not description:
                error = "Duty number and description are required"

            elif not number:
                error = "Invalid duty number"

            elif not description:
                error = "Invalid duty description"

            else:
                result = app.duty_service.create_duty(
                    number=number,
                    description=description
                )

                if result is None:
                    error = "Duplicate duty number"

        duties = app.duty_service.get_all_duties()

        formatted_duties = [
            f"{d['number']} - {d['description']}"
            for d in duties
        ]

        return render_template(
            "index.html",
            duties=formatted_duties,
            error=error
    )
    

    # -----------------------
    # Coins API
    # -----------------------
    
    @app.route("/coins", methods=["GET"])
    def get_all_coins():
        coins_response = app.coin_service.get_all_coins()
        return jsonify(coins_response), 200

    @app.route("/coins", methods=["POST"])
    def create_coin():
        coin_creation_data = request.get_json()
        new_coin = app.coin_service.create_coin(coin_creation_data["name"])

        if new_coin is None:
            return jsonify({"error": "Coin already exists"}), 400

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
    

# -----------------------
# Coin -> Duties (legacy API maintained alongside new DutyService)
# -----------------------
    @app.route("/coins/<coin_id>/duties", methods=["POST"])
    def create_duty_for_coin(coin_id):
        response_data = request.get_json()

        error = validate_duty_request(response_data)
        if error:
            return {"error": error}, 400
        
        result = app.coin_service.add_duty_to_coin(
            coin_id,
            response_data["duty_number"],
            response_data["description"]
        )

        error_responses = {
            "coin_not_found": ({"error": "Coin not found"}, 404),
            "duplicate_duty": ({"error": "Duty already exists"}, 409)
        }

        if result in error_responses:
            return error_responses[result]

        return {}, 201

# -----------------------
# Duties (NEW SYSTEM())
# -----------------------

    @app.route("/duties", methods=["GET"])
    def get_duties():
        duties_response = app.duty_service.get_all_duties()
        return jsonify(duties_response), 200
    
    @app.route("/duties", methods=["POST"])
    def create_duty():
        response_data = request.get_json()

        if "number" not in response_data and "description" not in response_data:
            return {"error": "Number and Description are required"}, 400

        if "number" not in response_data:
            return {"error": "Number is required"}, 400
        
        if "description" not in response_data:
            return {"error": "Description is required"}, 400

        result = app.duty_service.create_duty(
            number=response_data["number"],
            description=response_data["description"]
        )

        if result is None:
            return {"error": "Duty already exists"}, 400

        return {}, 201
    
    @app.route("/duties/<duty_id>", methods=["GET"])
    def get_duty_by_id(duty_id):
        duty = app.duty_service.get_duty_by_id(duty_id)

        if not duty:
            return {"error": "Duty not found"}, 404
        
        return duty, 200
    
    @app.route("/duties/<duty_id>", methods=["DELETE"])
    def delete_duty(duty_id):
        duty = app.duty_service.delete_duty(duty_id)

        if duty is None:
            return {"error": "Duty not found"}, 404
        
        return {}, 200
    
    @app.route("/duties/<duty_id>", methods=["PUT"])
    def update_duty(duty_id):
        duty = app.duty_service.update_duty(duty_id, request.get_json())

        if duty is None:
            return {"error": "Duty not found"}, 404
        
        if duty == "number_not_allowed":
            return {"error": "Duty number cannot be changed"}, 400

        return {}, 200
    
    return app

# -----------------------
# Entry point (dev only)
# -----------------------

app = create_app(
    InMemoryCoinRepository(),
    InMemoryDutyRepository()
)

# app = create_app(
#     DatabaseCoinRepository(),
#     DatabaseDutyRepository()
# )

    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
