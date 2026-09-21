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
    / "openrepair_core_access_device_barriers.csv"
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
        and row["repair_status"] == "End of life"
    ]

documented = [
    row for row in rows
    if row["repair_barrier_if_end_of_life"].strip()
]

counts = Counter(
    row["repair_barrier_if_end_of_life"]
    for row in documented
)

results = []

for barrier, count in counts.most_common():
    results.append({
        "barrier": barrier,
        "barrier_count": count,
        "pct_of_documented_barriers": round(
            count / len(documented) * 100,
            1
        ),
        "end_of_life_records": len(rows),
        "documented_barrier_records": len(documented),
        "barrier_documentation_pct": round(
            len(documented) / len(rows) * 100,
            1
        ),
    })

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "barrier",
            "barrier_count",
            "pct_of_documented_barriers",
            "end_of_life_records",
            "documented_barrier_records",
            "barrier_documentation_pct",
        ]
    )

    writer.writeheader()
    writer.writerows(results)

print(f"Created: {OUTPUT_FILE}")
print(f"Core access-device end-of-life records: {len(rows):,}")
print(f"Documented barriers: {len(documented):,}")
print(
    f"Barrier documentation rate: "
    f"{len(documented) / len(rows) * 100:.1f}%"
)
print()

for row in results:
    print(
        f"{row['barrier']}: "
        f"{row['barrier_count']:,} "
        f"({row['pct_of_documented_barriers']}%)"
    )