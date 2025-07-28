from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display
from pathlib import Path

# TODO: create a car park object with the location moondalup, capacity 100, and log_file "moondalup.txt"
# TODO: Write the car park configuration to a file called "moondalup_config.json"
# TODO: Reinitialize the car park object from the "moondalup_config.json" file
# TODO: create an entry sensor object with id 1, is_active True, and car_park car_park
# TODO: create an exit sensor object with id 2, is_active True, and car_park car_park
# TODO: create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park
# TODO: drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)
# TODO: drive 2 cars out of the car park (must be triggered via the sensor - NOT by calling car_park.remove_car directly)


def main():
    car_park = CarPark("Moondalup", 100, log_file=Path("moondalup.txt"))

    #Write the car park configuration to a JSON file
    car_park.config_file = Path("moondalup_config.json")  # update config file path
    car_park.write_config()

    #Reinitialize the car park object from the config file
    car_park = CarPark.from_config(config_file=Path("moondalup_config.json"))

    #Create and register an entry sensor
    entry_sensor = EntrySensor(id=1, is_active=True, car_park=car_park)
    car_park.register(entry_sensor)

    #Create and register an exit sensor
    exit_sensor = ExitSensor(id=2, is_active=True, car_park=car_park)
    car_park.register(exit_sensor)

    #Create and register a display
    display = Display(id=1, message="Welcome to Moondalup", is_on=True)
    car_park.register(display)

    #Simulate 10 cars entering
    for _ in range(10):
        entry_sensor.detect_vehicle()

    #Simulate 2 cars exiting
    for _ in range(2):
        exit_sensor.detect_vehicle()

if __name__ == "__main__":
    main()