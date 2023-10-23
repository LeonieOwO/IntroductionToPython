# Constants
class vehicle(object):
    air_density = 1.225  # kg/m³
    cross_sectional_area = 1.97  # m²
    drag_coefficient = 0.31
    velocity_kph = 80  # kilometers per hour
    velocity_ms = velocity_kph * 1000 / 3600  # Convert velocity to m/s
    rolling_resistance_coefficient = 0.015
    mass = 1500  # kg
    g = 9.81  # m/s²

# Calculate power consumption
    power_drag = 0.5 * air_density * cross_sectional_area * drag_coefficient * velocity_ms**3
    power_rolling_resistance = rolling_resistance_coefficient * mass * g * velocity_ms
    total_power = power_drag + power_rolling_resistance

# Print the result in kilowatts (kW)
    total_power_kW = total_power / 1000
    print(f"Power consumption at {velocity_kph} km/h is {total_power_kW:.2f} kW.")

    total_power_kw = total_power / 1000

    if total_power_kw < 10:
        print(f"Vehicle is energy efficient!")
    else:
        print(f"Vehicle isn't energy efficient!")



#cars = [vehicle]
cars = [
    {
        "id"
    }
]