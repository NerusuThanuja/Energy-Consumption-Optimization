from flask import Flask, render_template, request
from src.predict import predict_energy
from src.optimization import optimize

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    form_data = {}

    if request.method == "POST":
        form_data = {
            "hour": request.form["hour"],
            "temperature": request.form["temperature"],
            "humidity": request.form["humidity"],
            "load": request.form["load"],
            "occupancy": request.form["occupancy"],
        }

        energy, metrics = predict_energy(
            int(form_data["hour"]),
            float(form_data["temperature"]),
            float(form_data["humidity"]),
            float(form_data["load"]),
            int(form_data["occupancy"])
        )

        cost, tip = optimize(energy, float(form_data["temperature"]))

        result = {
            "energy": energy,
            "cost": cost,
            "tip": tip,
            "metrics": metrics
        }

    return render_template("index.html", result=result, form_data=form_data)

if __name__ == "__main__":
    app.run(debug=True)