import csv
from pathlib import Path

# Find the main Capstone Project folder based on this script's location.
PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = PROJECT_ROOT / "data" / "processed" / "ntia_2023_working.csv"
OUTPUT_FILE = PROJECT_ROOT / "analysis" / "results" / "ntia_age_technology_use.csv"

age_groups = {
    "3-17": lambda age: 3 <= age <= 17,
    "18-34": lambda age: 18 <= age <= 34,
    "35-49": lambda age: 35 <= age <= 49,
    "50-64": lambda age: 50 <= age <= 64,
    "65-74": lambda age: 65 <= age <= 74,
    "75+": lambda age: age >= 75,
}

variables = {
    "laptop_pct": "pelaptop",
    "desktop_pct": "pedesktp",
    "tablet_pct": "petablet",
    "smartphone_pct": "pemphone",
    "home_internet_pct": "peinhome",
}

with open(INPUT_FILE, newline="", encoding="utf-8") as file:
    rows = list(csv.DictReader(file))

results = []

for age_group, age_rule in age_groups.items():
    group_rows = [
        row for row in rows
        if age_rule(int(row["prtage"]))
    ]

    result = {"age_group": age_group}

    for output_name, variable in variables.items():
        yes_weight = sum(
            float(row["pwsswgt"])
            for row in group_rows
            if row[variable] == "1"
        )

        eligible_weight = sum(
            float(row["pwsswgt"])
            for row in group_rows
            if row[variable] in ("1", "2")
        )

        result[output_name] = round(
            yes_weight / eligible_weight * 100,
            1
        )

    results.append(result)

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["age_group"] + list(variables.keys())
    )
    writer.writeheader()
    writer.writerows(results)

print(f"Created: {OUTPUT_FILE}")