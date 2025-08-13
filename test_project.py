import unittest
import os
import json
import csv
from your_script_filename import csv_to_json, json_to_csv  # replace with actual file name

class TestCSVJSONConverter(unittest.TestCase):

    def setUp(self):
        # Create a sample CSV and JSON for testing
        self.csv_file = "test_data.csv"
        self.json_file = "test_data.json"

        with open(self.csv_file, "w", newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["name", "age"])
            writer.writeheader()
            writer.writerow({"name": "Alice", "age": "25"})
            writer.writerow({"name": "Bob", "age": "30"})

    def tearDown(self):
        # Cleanup test files
        for file in [self.csv_file, self.json_file]:
            if os.path.exists(file):
                os.remove(file)

    def test_csv_to_json(self):
        result = csv_to_json(self.csv_file, self.json_file)
        self.assertTrue(result)
        self.assertTrue(os.path.exists(self.json_file))

        with open(self.json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["name"], "Alice")

    def test_json_to_csv(self):
        # First create JSON from CSV
        csv_to_json(self.csv_file, self.json_file)

        # Convert back to CSV
        new_csv_file = "converted.csv"
        result = json_to_csv(self.json_file, new_csv_file)
        self.assertTrue(result)
        self.assertTrue(os.path.exists(new_csv_file))

        with open(new_csv_file, newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[1]["name"], "Bob")

        os.remove(new_csv_file)

if __name__ == "__main__":
    unittest.main()
