from flask import Flask, request, render_template
from duties import handle_create_duty

app = Flask(__name__)

duties = []

@app.route("/", methods=["GET", "POST"])
def home():
    global duties

    error = None

    if request.method == "POST":
        number = request.form.get("number")
        description = request.form.get("description")

        result = handle_create_duty(number, description, duties)

        if result["success"]:
            duties.append(result["duty"])
        else:
            error = result["error"]

    return render_template(
        "index.html",
        duties=duties,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
