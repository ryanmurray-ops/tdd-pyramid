from flask import Flask, request, render_template
from duties import create_duty

app = Flask(__name__)

duties = []

ERRORS = (
    "Invalid duty number",
    "Invalid duty description",
    "Duty number and description are required",
    "Duplicate duty number"
)

@app.route("/", methods=["GET", "POST"])
def home():
    global duties

    error = None

    if request.method == "POST":
        number = request.form.get("number")
        description = request.form.get("description")

        created_duty = create_duty(number, description, duties)

        if created_duty in ERRORS:
            error = created_duty
        else:
            duties.append(created_duty)

    return render_template(
        "index.html",
        duties=duties,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
