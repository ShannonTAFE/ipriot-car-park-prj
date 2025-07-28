import unittest
from pathlib import Path
import json
from car_park import CarPark  # adjust import if your structure is different


class TestCarParkConfig(unittest.TestCase):

    def setUp(self):
        # Setup file paths for temporary test files
        self.config_path = Path("temp_config.json")
        self.log_path = Path("temp_log.txt")

        # Create config file contents
        self.config_data = {
            "location": "Config Location",
            "capacity": 75,
            "log_file": str(self.log_path)
        }

        # Write JSON config
        with self.config_path.open("w") as f:
            json.dump(self.config_data, f)

    def test_config_initialization(self):
        # Create CarPark using from_config
        car_park = CarPark.from_config(self.config_path)

        # Assert CarPark attributes
        self.assertEqual(car_park.location, "Config Location")
        self.assertEqual(car_park.capacity, 75)
        self.assertEqual(car_park.plates, [])
        self.assertEqual(car_park.log_file, self.log_path)

    def tearDown(self):
        # Clean up test files
        self.config_path.unlink(missing_ok=True)
        self.log_path.unlink(missing_ok=True)