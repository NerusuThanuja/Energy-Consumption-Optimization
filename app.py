from flask import Flask, render_template, request
from src.predict import predict_energy

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        hour = int(request.form["hour"])
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        appliance_load = float(request.form["appliance_load"])
        occupancy = int(request.form["occupancy"])

        energy = predict_energy(
            hour, temperature, humidity, appliance_load, occupancy
        )

        cost = round(energy * 8.5, 2)

        recommendation = (
            "Shift heavy loads to afternoon to save ~15%"
            if hour >= 18 else
            "Energy usage is optimal"
        )

        result = {
            "energy": energy,
            "cost": cost,
            "recommendation": recommendation
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)