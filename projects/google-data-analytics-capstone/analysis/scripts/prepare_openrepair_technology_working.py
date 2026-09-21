import csv
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FOLDER = (
    PROJECT_ROOT
    / "Datasets"
    / "Open Repair Alliance"
    / "OpenRepairData_v0.3_aggregate_202507"
    / "202507"
    / "aggregate"
)

INPUT_FILE = next(
    INPUT_FOLDER.glob("OpenRepairData_v0.3_aggregate_202507*.csv")
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "openrepair_technology_working.csv"
)

technology_categories = {
    "Laptop",
    "Desktop computer",
    "Mobile",
    "Tablet",
    "Printer/scanner",
    "Flat screen",
    "Games console",
    "PC accessory",
    "Battery/charger/adapter",
    "TV and gaming-related accessories",
}

columns = [
    "id",
    "data_provider",
    "country",
    "product_category",
    "product_category_id",
    "brand",
    "year_of_manufacture",
    "product_age",
    "repair_status",
    "repair_barrier_if_end_of_life",
    "event_date",
    "problem",
]

count = 0

with open(INPUT_FILE, newline="", encoding="utf-8-sig") as source:
    reader = csv.DictReader(source)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as output:
        writer = csv.DictWriter(output, fieldnames=columns)
        writer.writeheader()

        for row in reader:
            if row["product_category"] not in technology_categories:
                continue

            writer.writerow({
                column: row[column]
                for column in columns
            })

            count += 1

print(f"Created: {OUTPUT_FILE}")
print(f"Technology records: {count:,}")
print(f"Columns: {len(columns)}")