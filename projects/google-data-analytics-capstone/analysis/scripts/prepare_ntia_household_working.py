import csv
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = (
    PROJECT_ROOT
    / "Datasets"
    / "NTIA Internet Usage Survey"
    / "CSV Files"
    / "nov23-cps-csv"
    / "nov23-cps.csv"
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "ntia_2023_household_working.csv"
)

columns = [
    "hrhhid2",
    "gestfips",
    "hefaminc",
    "hwhhwgt",
    "helaptop",
    "hedesktp",
    "hetablet",
    "hemphone",
    "heinhome",
]

count = 0

with open(INPUT_FILE, newline="", encoding="utf-8-sig") as source:
    reader = csv.DictReader(source)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as output:
        writer = csv.DictWriter(output, fieldnames=columns)
        writer.writeheader()

        for row in reader:
            # PERRP 40 and 41 identify the household reference person.
            # Keeping only these records gives one record per household.
            if row["perrp"] not in ("40", "41"):
                continue

            writer.writerow({
                column: row[column]
                for column in columns
            })

            count += 1

print(f"Created: {OUTPUT_FILE}")
print(f"Household rows: {count:,}")
print(f"Columns: {len(columns)}")