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
    / "ntia_education_digital_engagement.csv"
)

education_groups = {
    "Less than high school": {"31", "32", "33", "34", "35", "36", "37", "38"},
    "High school / GED": {"39"},
    "Some college / associate": {"40", "41", "42"},
    "Bachelor's degree": {"43"},
    "Graduate / professional": {"44", "45", "46"},
}

variables = {
    "email_pct": "peemail",
    "financial_services_pct": "pefinanc",
    "government_services_pct": "peegovts",
    "education_job_training_pct": "peedtrai",
}

with open(INPUT_FILE, newline="", encoding="utf-8") as file:
    rows = [
        row for row in csv.DictReader(file)
        if int(row["prtage"]) >= 25
    ]

results = []

for education_group, education_codes in education_groups.items():
    group_rows = [
        row for row in rows
        if row["peeduca"] in education_codes
    ]

    result = {
        "education_group": education_group,
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
            "education_group",
            "sample_records",
        ] + list(variables.keys())
    )

    writer.writeheader()
    writer.writerows(results)

print(f"Created: {OUTPUT_FILE}")