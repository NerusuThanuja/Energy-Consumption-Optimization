from flask import Flask, render_template, request

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

        # ---- Simple deterministic logic (no ML model) ----
        energy = round(
            (appliance_load * 1.8) +
            (occupancy * 0.6) +
            (temperature * 0.12) +
            (humidity * 0.05),
            2
        )

        cost = round(energy * 8.5, 2)  # ₹ per kWh
        carbon_emission = round(energy * 0.82, 2)  # kg CO2 (approx)

        if hour >= 18:
            recommendation = "Shift heavy loads to afternoon to save ~15%"
            efficiency = "Moderate"
        else:
            recommendation = "Energy usage is optimal"
            efficiency = "High"

        result = {
            "energy": energy,
            "cost": cost,
            "carbon": carbon_emission,
            "efficiency": efficiency,
            "recommendation": recommendation
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)