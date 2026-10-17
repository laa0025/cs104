# My car: 2023 BMW M5 Competition Sedan, 4.4L V8

import csv

make = "BMW"
model = "M5 Competition Sedan"

fields = ["make", "model", "year", "trany", "drive", "cylinders",
          "displ", "city08", "highway08", "co2TailpipeGpm"]

cars = []

with open("vehicles.csv", "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["make"] == make and row["model"] == model and int(row["year"]) <= 2025:
            cars.append({field: row[field] for field in fields})

cars.sort(key=lambda car: int(car["year"]))

for car in cars:
    print("Year:", car["year"])
    print("Make:", car["make"])
    print("Model:", car["model"])
    print("Transmission:", car["trany"])
    print("Drive:", car["drive"])
    print("Cylinders:", car["cylinders"])
    print("Engine size:", car["displ"], "L")
    print("City MPG:", car["city08"])
    print("Highway MPG:", car["highway08"])
    print("CO2 emissions:", car["co2TailpipeGpm"], "grams/mile")
    print()

with open("BMW_M5_Competition_Sedan.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(cars)

print("Saved", len(cars), "records to BMW_M5_Competition_Sedan.csv")
