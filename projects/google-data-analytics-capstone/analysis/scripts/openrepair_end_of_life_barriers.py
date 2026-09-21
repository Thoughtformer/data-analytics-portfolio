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
    / "openrepair_end_of_life_barriers.csv"
)

with open(INPUT_FILE, newline="", encoding="utf-8") as file:
    rows = list(csv.DictReader(file))

categories = sorted(
    set(row["product_category"] for row in rows)
)

scopes = [("All technology", rows)]

for category in categories:
    category_rows = [
        row for row in rows
        if row["product_category"] == category
    ]

    scopes.append((category, category_rows))

results = []

for scope_name, scope_rows in scopes:

    end_of_life = [
        row for row in scope_rows
        if row["repair_status"] == "End of life"
    ]

    documented = [
        row for row in end_of_life
        if row["repair_barrier_if_end_of_life"].strip()
    ]

    counts = Counter(
        row["repair_barrier_if_end_of_life"]
        for row in documented
    )

    documentation_pct = (
        len(documented) / len(end_of_life) * 100
        if end_of_life
        else 0
    )

    for barrier, count in counts.most_common():

        barrier_pct = (
            count / len(documented) * 100
            if documented
            else 0
        )

        results.append({
            "scope": scope_name,
            "end_of_life_records": len(end_of_life),
            "documented_barrier_records": len(documented),
            "barrier_documentation_pct": round(
                documentation_pct, 1
            ),
            "barrier": barrier,
            "barrier_count": count,
            "barrier_pct_of_documented": round(
                barrier_pct, 1
            ),
        })

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "scope",
            "end_of_life_records",
            "documented_barrier_records",
            "barrier_documentation_pct",
            "barrier",
            "barrier_count",
            "barrier_pct_of_documented",
        ]
    )

    writer.writeheader()
    writer.writerows(results)

print(f"Created: {OUTPUT_FILE}")
print()

for row in results:
    if row["scope"] == "All technology":
        print(
            f"{row['barrier']}: "
            f"{row['barrier_count']:,} "
            f"({row['barrier_pct_of_documented']}% "
            f"of documented barriers)"
        )