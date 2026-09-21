import csv
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = (
    PROJECT_ROOT
    / "Datasets"
    / "NTIA Internet Usage Survey"
    / "CSV Files"
    / "nov23-cps-csv"
    / "nov23-cps.csv"
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "ntia_2023_random_respondent_working.csv"
)

columns = [
    "hrhhid2",
    "gestfips",
    "prtage",
    "pesex",
    "peeduca",
    "hefaminc",
    "pemlr",
    "ptdtrace",
    "pwprmwgt",
    "pelaptop",
    "pemphone",
    "peinhome",
    "peemail",
    "pefinanc",
    "peegovts",
    "peedtrai",
]

count = 0

with open(INPUT_FILE, newline="", encoding="utf-8-sig") as source:
    reader = csv.DictReader(source)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as output:
        writer = csv.DictWriter(output, fieldnames=columns)
        writer.writeheader()

        for row in reader:
            # Keep only respondents eligible for the random-respondent
            # internet activity questions.
            if row["peemail"] not in ("1", "2"):
                continue

            if float(row["pwprmwgt"]) <= 0:
                continue

            writer.writerow({
                column: row[column]
                for column in columns
            })

            count += 1

print(f"Created: {OUTPUT_FILE}")
print(f"Random respondent rows: {count:,}")
print(f"Columns: {len(columns)}")