from vehicle import Vehicle
import json
import logging

#def load_vehicles_from_json(file_path):
    #with open("vehicles.json", "r") as file:
      #  data = json.load(file)
     #   vehicles = [Vehicle(**vehicle_data) for vehicle_data in data]
    #return vehicles


if __name__ == "__main__":

    #json_file_path = 'vehicles.json'  # Setze deinen Dateipfad hier ein
    #vehicles = load_vehicles_from_json(json_file_path)

    #print(Vehicle.count)
    #print(Vehicle.power_cons)
    logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d \
        ::\n%(message)s', level = logging.INFO)
    

    #air_density = 0
    #mass = 0
    vehicle = Vehicle(air_density= 1, mass = 3000 )
    #logging.info(Vehicle.count)
    logging.info("Vehicle: %s", vehicle)
    logging.info("Power Consumption: %s", vehicle.power_cons)
    #logging.info(air_density, mass, vehicle)
    
    print(vehicle)
    print(vehicle.power_cons)
    
    vehicle=Vehicle.add_vehicle(air_density= 1.2, mass=2000)
    print(vehicle)
    print(vehicle.power_cons)
    