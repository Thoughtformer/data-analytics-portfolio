import csv
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "ntia_2023_random_respondent_working.csv"
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "analysis"
    / "results"
    / "ntia_age_income_digital_engagement.csv"
)

age_groups = {
    "18-64": lambda age: 18 <= age <= 64,
    "65+": lambda age: age >= 65,
}

income_groups = {
    "Under $25k": {"1", "2", "3", "4", "5", "6", "7"},
    "$25k-$49,999": {"8", "9", "10", "11"},
    "$50k-$74,999": {"12", "13"},
    "$75k-$99,999": {"14"},
    "$100k-$149,999": {"15"},
    "$150k+": {"16"},
}

variables = {
    "email_pct": "peemail",
    "financial_services_pct": "pefinanc",
    "government_services_pct": "peegovts",
    "education_job_training_pct": "peedtrai",
}

with open(INPUT_FILE, newline="", encoding="utf-8") as file:
    rows = list(csv.DictReader(file))

results = []

for income_group, income_codes in income_groups.items():
    for age_group, age_rule in age_groups.items():

        group_rows = [
            row for row in rows
            if row["hefaminc"] in income_codes
            and age_rule(int(row["prtage"]))
        ]

        result = {
            "income_group": income_group,
            "age_group": age_group,
            "sample_records": len(group_rows),
        }

        for output_name, variable in variables.items():
            yes_weight = sum(
                float(row["pwprmwgt"])
                for row in group_rows
                if row[variable] == "1"
            )

            eligible_weight = sum(
                float(row["pwprmwgt"])
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
        fieldnames=[
            "income_group",
            "age_group",
            "sample_records",
        ] + list(variables.keys())
    )

    writer.writeheader()
    writer.writerows(results)

print(f"Created: {OUTPUT_FILE}")