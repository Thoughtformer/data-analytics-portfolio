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
    / "openrepair_category_outcomes.csv"
)

with open(INPUT_FILE, newline="", encoding="utf-8") as file:
    rows = list(csv.DictReader(file))

categories = sorted(
    set(row["product_category"] for row in rows)
)

results = []

for category in categories:
    group_rows = [
        row for row in rows
        if row["product_category"] == category
    ]

    counts = Counter(
        row["repair_status"]
        for row in group_rows
    )

    total = len(group_rows)

    fixed = counts["Fixed"]
    repairable = counts["Repairable"]
    end_of_life = counts["End of life"]
    unknown = counts["Unknown"]

    results.append({
        "product_category": category,
        "records": total,
        "fixed_pct": round(fixed / total * 100, 1),
        "repairable_pct": round(repairable / total * 100, 1),
        "fixed_or_repairable_pct": round(
            (fixed + repairable) / total * 100,
            1
        ),
        "end_of_life_pct": round(
            end_of_life / total * 100,
            1
        ),
        "unknown_pct": round(
            unknown / total * 100,
            1
        ),
    })

results.sort(
    key=lambda row: row["fixed_or_repairable_pct"],
    reverse=True
)

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "product_category",
            "records",
            "fixed_pct",
            "repairable_pct",
            "fixed_or_repairable_pct",
            "end_of_life_pct",
            "unknown_pct",
        ]
    )

    writer.writeheader()
    writer.writerows(results)

print(f"Created: {OUTPUT_FILE}")
print()

for row in results:
    print(
        f"{row['product_category']}: "
        f"{row['fixed_or_repairable_pct']}% "
        f"fixed or repairable"
    )