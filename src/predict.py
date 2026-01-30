def predict_energy(hour, temperature, humidity, appliance_load, occupancy):
    """
    Rule-based energy estimation (NO ML MODEL)
    """

    # base load
    energy = 0.5

    # time-based usage
    if 6 <= hour <= 9:
        energy += 0.6
    elif 18 <= hour <= 23:
        energy += 0.8

    # temperature effect
    if temperature > 30:
        energy += 0.7
    elif temperature < 18:
        energy += 0.5

    # humidity effect
    if humidity > 70:
        energy += 0.3

    # appliance load (kW)
    energy += appliance_load * 0.4

    # occupancy
    energy += occupancy * 0.2

    return round(energy, 2)