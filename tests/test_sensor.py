# test_sensor.py
import unittest
from sensor import EntrySensor, ExitSensor
from car_park import CarPark

# For mocking random numbers
from unittest.mock import patch


class TestSensors(unittest.TestCase):

    def setUp(self):
        # Create a car park for testing
        self.car_park = CarPark("Test Location", 10)

    def test_entry_sensor_adds_car(self):
        # Make an EntrySensor attached to the test car park
        entry_sensor = EntrySensor(1, self.car_park)

        # Make sure it adds a specific plate by mocking random.randint
        with patch("sensor.random.randint", return_value=101):
            entry_sensor.detect_vehicle()

        # Check that plate "FAKE-101" was added
        self.assertIn("FAKE-101", self.car_park.plates)

    def test_exit_sensor_removes_car(self):
        # Add a fake car to simulate it's in the car park
        self.car_park.plates.append("FAKE-222")

        # Make an ExitSensor
        exit_sensor = ExitSensor(2, self.car_park)

        # Make sure it tries to remove that exact plate
        with patch("sensor.random.choice", return_value="FAKE-222"):
            exit_sensor.detect_vehicle()

        # Check that plate was removed
        self.assertNotIn("FAKE-222", self.car_park.plates)