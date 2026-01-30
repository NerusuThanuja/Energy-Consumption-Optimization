def optimize(energy, temperature):
    cost = energy * 6.5  # ₹/kWh

    comfort_penalty = 0
    if temperature < 18 or temperature > 24:
        comfort_penalty = 20

    if energy > 2:
        recommendation = "Shift heavy loads to afternoon to save ~15%"
    else:
        recommendation = "Energy usage is optimal"

    return round(cost + comfort_penalty, 2), recommendation