# SQL Analysis

This folder contains Structured Query Language (SQL) analyses used to independently reproduce and validate selected headline findings from the capstone in Google BigQuery.

Python was used primarily for data preparation, exploratory analysis, reproducible processing, and initial result generation.

SQL was then used as a second analytical workflow to validate selected findings directly from the processed datasets.

The SQL work is intentionally focused. It does not reimplement every Python analysis.

---

## BigQuery Environment

Google Cloud project:

`data-analytics-capstone-509318`

BigQuery dataset:

`capstone_analysis`

Current BigQuery tables:

- `openrepair_technology`
- `ntia_2023_household`

Full table paths:

`data-analytics-capstone-509318.capstone_analysis.openrepair_technology`

`data-analytics-capstone-509318.capstone_analysis.ntia_2023_household`

---

## Source Datasets

### Open Repair Alliance

Local processed dataset:

`data/processed/openrepair_technology_working.csv`

BigQuery table:

`capstone_analysis.openrepair_technology`

Records:

47,024

The BigQuery table was created using an explicit schema because automatic schema detection incorrectly classified `product_age` as an integer even though decimal values were present.

Important field types include:

- `product_category_id` — INTEGER
- `year_of_manufacture` — INTEGER
- `product_age` — FLOAT
- `event_date` — DATE

---

### National Telecommunications and Information Administration (NTIA)

Local processed household dataset:

`data/processed/ntia_2023_household_working.csv`

BigQuery table:

`capstone_analysis.ntia_2023_household`

Household records:

42,204

The household survey weight is:

`HWHHWGT`

In BigQuery the corresponding field is stored as:

`hwhhwgt`

Important household technology-use fields include:

- `helaptop`
- `hedesktp`
- `hetablet`
- `hemphone`
- `heinhome`

Household/family income category is stored as:

`hefaminc`

---

## SQL Skills Demonstrated

The completed SQL analyses demonstrate use of:

- `SELECT`
- `FROM`
- `WHERE`
- `IN`
- `AND`
- `BETWEEN`
- `CASE`
- `GROUP BY`
- `ORDER BY`
- `COUNT`
- `COUNTIF`
- `SUM`
- aliases with `AS`
- conditional aggregation
- percentage calculations
- window aggregation
- weighted survey calculations
- explicit valid-response denominators

---

## Completed SQL Analyses

### `openrepair_core_device_outcomes.sql`

Analyzes repair outcomes for the four core digital-access device categories:

- Laptop
- Desktop computer
- Mobile
- Tablet

The SQL filter identifies 23,612 repair-event records.

Validated counts:

- Fixed: 12,493
- Repairable: 6,205
- End of life: 4,047
- Unknown: 867
- Fixed or repairable: 18,698

Validated combined fixed-or-repairable share:

79.2%

`Repairable` does not mean that a repair was completed. It indicates that reasonable next steps toward repair were identified.

Corresponding result:

`analysis/results/openrepair_core_device_outcomes_sql.csv`

---

### `openrepair_core_device_barriers.sql`

Analyzes documented end-of-life repair barriers for core digital-access devices.

Validated population:

- End-of-life records: 4,047
- Records with a documented barrier: 1,173
- Barrier documentation rate: 29.0%

Among records with a documented barrier:

- Spare parts too expensive: 24.4%
- Repair information not available: 19.8%
- Spare parts not available: 16.1%
- Lack of equipment: 14.7%
- No way to open product: 13.1%
- Item too worn out: 11.9%

Because barrier information is missing for 71.0% of end-of-life records, these percentages apply only to records where a barrier was documented.

Corresponding result:

`analysis/results/openrepair_core_device_barriers_sql.csv`

---

### `ntia_household_income_technology_use.sql`

Reproduces weighted household technology-use estimates by household/family income using the NTIA 2023 household working dataset.

The analysis demonstrates survey weighting rather than simple row counting.

The general weighted percentage structure is:

`SUM(weight × indicator) / SUM(weight)`

The final query uses variable-specific valid-response denominators so that only eligible Yes/No responses contribute to each weighted estimate.

Validated household laptop-use estimates:

- Under $25,000: 41.2%
- $25,000–$49,999: 54.9%
- $50,000–$74,999: 69.0%
- $75,000–$99,999: 76.5%
- $100,000–$149,999: 80.6%
- $150,000+: 84.6%

The same query also reproduces weighted estimates for:

- Desktop computer use
- Tablet use
- Mobile-phone use
- Home internet use

Corresponding result:

`analysis/results/ntia_household_income_technology_use_sql.csv`

---

## SQL Validation Strategy

The SQL analyses are not separate external evidence.

They operate on the same processed datasets used by the Python analyses.

Their purpose is to:

1. independently reproduce selected findings
2. demonstrate SQL competency
3. verify important headline calculations through a second analytical workflow
4. provide readable, reproducible portfolio examples

Agreement between Python and SQL outputs increases confidence that the selected transformations and calculations were implemented consistently.

It does not eliminate limitations in the underlying source data.

---

## Survey Weighting

The NTIA household analysis uses the household survey weight:

`HWHHWGT`

A simple unweighted row percentage would treat every sampled household as equally representative of the population.

The weighted calculation instead incorporates each household's survey weight.

Conceptually:

`weighted percentage = weighted Yes responses / weighted eligible responses`

The final SQL queries use conditional aggregation so that invalid or ineligible response codes are excluded from the relevant denominator rather than treated as No responses.

---

## Open Repair Interpretation

Open Repair Alliance data represent devices brought to participating community repair organizations and events.

The data are:

- observational
- self-selected
- heavily European
- not representative of all discarded electronics
- not representative of U.S. households

The SQL results therefore validate calculations within this dataset but do not establish population-level repair rates.

---

## Result Files

SQL-generated result CSVs are stored in the existing shared results folder:

`analysis/results/`

SQL result files use the suffix:

`_sql.csv`

Examples:

- `openrepair_core_device_outcomes_sql.csv`
- `openrepair_core_device_barriers_sql.csv`
- `ntia_household_income_technology_use_sql.csv`

There is no separate SQL results hierarchy.

This keeps all analytical outputs in one location while distinguishing SQL validation results from Python-generated results.
