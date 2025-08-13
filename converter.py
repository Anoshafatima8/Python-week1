import csv
import json

def csv_to_json(csv_file, json_file):
    """Convert CSV to JSON."""
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print(f"CSV → JSON conversion complete: {json_file}")

def json_to_csv(json_file, csv_file):
    """Convert JSON to CSV."""
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Ensure JSON is a list of dictionaries
    if not isinstance(data, list) or not all(isinstance(i, dict) for i in data):
        raise ValueError("JSON must be a list of objects (dictionaries)")

    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"JSON → CSV conversion complete: {csv_file}")


# Example usage:
# CSV to JSON
csv_to_json("grades.csv", "grades.json")

# JSON to CSV
json_to_csv("grades.json", "grades_converted.csv")
