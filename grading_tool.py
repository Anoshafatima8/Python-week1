import csv

# Step 1: Read the CSV file
students = []
with open("grades.csv", "r") as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        students.append({"Name": row["Name"], "Grade": float(row["Grade"])})

# Step 2: Calculate the average grade
def calculate_average(csv_file):
    """Calculate average grade from a CSV file with 'Grade' column."""
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        grades = [float(row["Grade"]) for row in reader]
    return sum(grades) / len(grades) if grades else 0


# Step 3: Determine Pass/Fail and write to new CSV
with open("results.csv", "w", newline="") as outfile:
    fieldnames = ["Name", "Grade", "Result"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for student in students:
        result = "Pass" if student["Grade"] >= 50 else "Fail"
        writer.writerow({
            "Name": student["Name"],
            "Grade": student["Grade"],
            "Result": result
        })

print("Results written to results.csv")
