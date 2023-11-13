from vehicle import Vehicle

if __name__ == "__main__":
    print(Vehicle.count)
    vehicle = Vehicle(air_density= 1, mass = 3000 )
    print(vehicle)
    print(vehicle.power_cons)
    
    vehicle=Vehicle.add_vehicle(air_density= 1.2, mass=2000)
    print(vehicle)
    print(vehicle.power_cons)
    