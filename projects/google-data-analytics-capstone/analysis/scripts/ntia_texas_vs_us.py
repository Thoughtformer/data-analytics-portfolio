import csv
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

PERSON_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "ntia_2023_working.csv"
)

RANDOM_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "ntia_2023_random_respondent_working.csv"
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "analysis"
    / "results"
    / "ntia_texas_vs_us.csv"
)

TEXAS_FIPS = "48"

person_variables = {
    "Laptop": "pelaptop",
    "Smartphone": "pemphone",
    "Internet at home": "peinhome",
}

random_variables = {
    "Financial services": "pefinanc",
    "Government services": "peegovts",
}


def weighted_percent(rows, variable, weight):
    yes_weight = sum(
        float(row[weight])
        for row in rows
        if row[variable] == "1"
    )

    eligible_weight = sum(
        float(row[weight])
        for row in rows
        if row[variable] in ("1", "2")
    )

    return yes_weight / eligible_weight * 100


results = []

with open(PERSON_FILE, newline="", encoding="utf-8") as file:
    person_rows = [
        row for row in csv.DictReader(file)
        if int(row["prtage"]) >= 18
    ]

texas_person = [
    row for row in person_rows
    if row["gestfips"] == TEXAS_FIPS
]

for label, variable in person_variables.items():
    us_pct = weighted_percent(
        person_rows,
        variable,
        "pwsswgt"
    )

    texas_pct = weighted_percent(
        texas_person,
        variable,
        "pwsswgt"
    )

    results.append({
        "indicator": label,
        "analysis_type": "Technology use",
        "us_pct": round(us_pct, 1),
        "texas_pct": round(texas_pct, 1),
        "texas_gap_pp": round(texas_pct - us_pct, 1),
        "us_sample_records": len(person_rows),
        "texas_sample_records": len(texas_person),
    })


with open(RANDOM_FILE, newline="", encoding="utf-8") as file:
    random_rows = [
        row for row in csv.DictReader(file)
        if int(row["prtage"]) >= 18
    ]

texas_random = [
    row for row in random_rows
    if row["gestfips"] == TEXAS_FIPS
]

for label, variable in random_variables.items():
    us_pct = weighted_percent(
        random_rows,
        variable,
        "pwprmwgt"
    )

    texas_pct = weighted_percent(
        texas_random,
        variable,
        "pwprmwgt"
    )

    results.append({
        "indicator": label,
        "analysis_type": "Digital engagement",
        "us_pct": round(us_pct, 1),
        "texas_pct": round(texas_pct, 1),
        "texas_gap_pp": round(texas_pct - us_pct, 1),
        "us_sample_records": len(random_rows),
        "texas_sample_records": len(texas_random),
    })


with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "indicator",
            "analysis_type",
            "us_pct",
            "texas_pct",
            "texas_gap_pp",
            "us_sample_records",
            "texas_sample_records",
        ]
    )

    writer.writeheader()
    writer.writerows(results)

print(f"Created: {OUTPUT_FILE}")