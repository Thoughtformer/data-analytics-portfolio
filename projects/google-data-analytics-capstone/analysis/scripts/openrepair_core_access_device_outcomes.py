import csv
from pathlib import Path
from collections import Counter

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "openrepair_technology_working.csv"
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "analysis"
    / "results"
    / "openrepair_core_access_device_outcomes.csv"
)

core_categories = {
    "Laptop",
    "Desktop computer",
    "Mobile",
    "Tablet",
}

with open(INPUT_FILE, newline="", encoding="utf-8") as file:
    rows = [
        row for row in csv.DictReader(file)
        if row["product_category"] in core_categories
    ]

counts = Counter(
    row["repair_status"]
    for row in rows
)

total = len(rows)

results = []

for status in [
    "Fixed",
    "Repairable",
    "End of life",
    "Unknown",
]:
    count = counts[status]

    results.append({
        "repair_status": status,
        "records": count,
        "percentage": round(count / total * 100, 1),
    })

fixed_or_repairable = (
    counts["Fixed"] + counts["Repairable"]
)

results.append({
    "repair_status": "Fixed or repairable",
    "records": fixed_or_repairable,
    "percentage": round(
        fixed_or_repairable / total * 100,
        1
    ),
})

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "repair_status",
            "records",
            "percentage",
        ]
    )

    writer.writeheader()
    writer.writerows(results)

print(f"Created: {OUTPUT_FILE}")
print(f"Core access-device records: {total:,}")
print()

for row in results:
    print(
        f"{row['repair_status']}: "
        f"{row['records']:,} "
        f"({row['percentage']}%)"
    )