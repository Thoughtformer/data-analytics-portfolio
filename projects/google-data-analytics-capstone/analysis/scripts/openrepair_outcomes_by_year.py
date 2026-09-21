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
    / "openrepair_outcomes_by_year.csv"
)

with open(INPUT_FILE, newline="", encoding="utf-8") as file:
    rows = list(csv.DictReader(file))

results = []

for year in range(2016, 2025):
    year_rows = [
        row for row in rows
        if row["event_date"][:4] == str(year)
    ]

    counts = Counter(
        row["repair_status"]
        for row in year_rows
    )

    total = len(year_rows)

    fixed = counts["Fixed"]
    repairable = counts["Repairable"]
    end_of_life = counts["End of life"]
    unknown = counts["Unknown"]

    results.append({
        "year": year,
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

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "year",
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
        f"{row['year']}: "
        f"{row['fixed_or_repairable_pct']}% fixed or repairable, "
        f"{row['end_of_life_pct']}% end of life"
    )