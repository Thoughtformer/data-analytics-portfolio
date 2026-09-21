import csv
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "ntia_2023_household_working.csv"
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "analysis"
    / "results"
    / "ntia_household_income_technology_use.csv"
)

income_groups = {
    "Under $25k": {"1", "2", "3", "4", "5", "6", "7"},
    "$25k-$49,999": {"8", "9", "10", "11"},
    "$50k-$74,999": {"12", "13"},
    "$75k-$99,999": {"14"},
    "$100k-$149,999": {"15"},
    "$150k+": {"16"},
}

variables = {
    "laptop_pct": "helaptop",
    "desktop_pct": "hedesktp",
    "tablet_pct": "hetablet",
    "mobile_phone_pct": "hemphone",
    "home_internet_pct": "heinhome",
}

with open(INPUT_FILE, newline="", encoding="utf-8") as file:
    rows = list(csv.DictReader(file))

results = []

for income_group, income_codes in income_groups.items():
    group_rows = [
        row for row in rows
        if row["hefaminc"] in income_codes
    ]

    result = {
        "income_group": income_group,
        "household_records": len(group_rows),
    }

    for output_name, variable in variables.items():
        yes_weight = sum(
            float(row["hwhhwgt"])
            for row in group_rows
            if row[variable] == "1"
        )

        total_weight = sum(
            float(row["hwhhwgt"])
            for row in group_rows
            if row[variable] in ("1", "2")
        )

        result[output_name] = round(
            yes_weight / total_weight * 100,
            1
        )

    results.append(result)

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "income_group",
            "household_records",
        ] + list(variables.keys())
    )

    writer.writeheader()
    writer.writerows(results)

print(f"Created: {OUTPUT_FILE}")