from flask import Flask, request, render_template
from duties import handle_create_duty
from services.duty_service import DutyService

app = Flask(__name__)

service = DutyService()

app.service = service

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

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
