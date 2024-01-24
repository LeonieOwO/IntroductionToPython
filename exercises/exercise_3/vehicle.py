class Vehicle(object):

#air_density = 1.225  # kg/m³
    cross_sectional_area = 1.97  # m²
    drag_coefficient = 0.31
    velocity_kph = 80  # kilometers per hour
    velocity_ms = velocity_kph * 1000 / 3600  # Convert velocity to m/s
    rolling_resistance_coefficient = 0.015
    #mass = 1500  # kg
    g = 9.81  # m/s²
    count = 0

    def __init__(self, air_density, mass):
        self.air_density = air_density
        self.mass = mass
        Vehicle.count += 1

    @property  #sorgt dafür, dass ich wie auf n Attribut zugreifen kann statt get_age einfach age
    def power_cons(self):
        #return self.air_density 
        power_drag = 0.5 * self.air_density * self.cross_sectional_area * self.drag_coefficient * self.velocity_ms**3
        power_rolling_resistance = self.rolling_resistance_coefficient * self.mass * self.g * self.velocity_ms
        total_power = power_drag + power_rolling_resistance
        total_power_kw = total_power / 1000
        
        print(f"Power consumption at {self.velocity_kph} km/h is {total_power_kw:.2f} kW.")

        #total_power_kw = total_power / 1000

        if total_power_kw < 10:
            print(f"Vehicle is energy efficient!")
        else:
            print(f"Vehicle isn't energy efficient!")
    


    @classmethod
    def add_vehicle(cls, air_density, mass):
        return cls(air_density, mass)
        

    def __str__(self):
        return f"air_density: {self.air_density}, Mass: {self.mass}"