from flask import Flask, request
from duties import is_duplicate_duty_number

app = Flask(__name__)

duties = []

@app.route("/", methods=["GET", "POST"])
def home():
    global duties

    if request.method == "POST":
        number = request.form.get("number")
        description = request.form.get("description")

        new_duty = f"{number} - {description}"

        is_duplicate = is_duplicate_duty_number(number, duties)

        if not is_duplicate:
            duties.append(new_duty)

    duties_html = ""

    for duty in duties:
        duties_html += f"<li>{duty}</li>"

    return f"""
    <h1>Automate Coin</h1>

    <div id="duties-section">

        <form method="POST">
            <label for="duty-number-input">Duty Number</label>
            <input id ="duty-number-input" name="number" />

            <label for="duty-description-input">Duty Description</label>
            <input id ="duty-description-input" name="description" />

            <button type="submit">Add Duty</button>
        </form>

        <ul id="duties-list">
            {duties_html}
        </ul>

    </div>
    """

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
