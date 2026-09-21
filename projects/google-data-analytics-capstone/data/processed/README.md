# Processed Data

This folder contains cleaned, filtered, or reduced datasets created from original public source data for analysis.

Original source files are preserved separately and are not overwritten.

---

## P01 — NTIA 2023 Working Dataset

**File:** `ntia_2023_working.csv`

**Source dataset:** NTIA 2023 Internet Use Survey (`nov23-cps.csv`)

**Source records:** 126,917  
**Source variables:** 1,037

**Processed records:** 96,532  
**Processed variables:** 15

### Processing Criteria

The working dataset includes only records that:

- Have a positive `PWSSWGT` person survey weight
- Represent civilian household members
- Are age 3 or older
- Fall within the eligible universe for the NTIA Internet Use Supplement

This reduced the source file from 126,917 records to 96,532 eligible person-level records.

### Variables Retained

| Variable | Purpose |
|---|---|
| `hrhhid2` | Household identifier |
| `gestfips` | State identifier |
| `prtage` | Age |
| `pesex` | Sex |
| `peeduca` | Educational attainment |
| `hefaminc` | Family / household income category |
| `pemlr` | Labor-force status |
| `ptdtrace` | Race |
| `pwsswgt` | General person survey weight |
| `pwprmwgt` | Random-respondent survey weight |
| `pelaptop` | Laptop use |
| `pedesktp` | Desktop computer use |
| `petablet` | Tablet use |
| `pemphone` | Smartphone use |
| `peinhome` | Internet use at home |

### Important Notes

- The original `nov23-cps.csv` file remains unchanged.
- Survey codes will be interpreted using the official NTIA / Census documentation.
- Negative survey codes such as `-1` will not automatically be treated as "No."
- Weighted estimates will use the survey weight appropriate to each variable.
- This working file is a reduced analytical extract, not a replacement for the original source dataset.


### `ntia_2023_household_working.csv`

Household-level working dataset derived from the November 2023 NTIA Internet Use Survey / Current Population Survey file.

The source file contains person-level records, so this extract keeps only household reference-person records (`PERRP` codes `40` and `41`) to produce one record per household.

- Source file: `nov23-cps.csv`
- Household records: 42,204
- Variables retained: 9
- Weight: `HWHHWGT`

Retained variables:

| Variable | Description |
|---|---|
| `hrhhid2` | Household identifier |
| `gestfips` | State FIPS code |
| `hefaminc` | Household/family income category |
| `hwhhwgt` | Household survey weight |
| `helaptop` | Household laptop use |
| `hedesktp` | Household desktop use |
| `hetablet` | Household tablet use |
| `hemphone` | Household mobile-phone use |
| `heinhome` | Household internet use at home |

The raw source file remains unchanged.

This processed dataset can be recreated using:

`analysis/scripts/prepare_ntia_household_working.py`


### `ntia_2023_random_respondent_working.csv`

Working dataset derived from the November 2023 NTIA Internet Use Survey / Current Population Survey file for questions asked only of the randomly selected household respondent.

The extract keeps only respondents eligible for the random-respondent internet activity questions and requires a positive `PWPRMWGT` weight.

- Source file: `nov23-cps.csv`
- Random respondent records: 36,648
- Variables retained: 16
- Weight: `PWPRMWGT`

Retained variables:

| Variable | Description |
|---|---|
| `hrhhid2` | Household identifier |
| `gestfips` | State FIPS code |
| `prtage` | Age |
| `pesex` | Sex |
| `peeduca` | Educational attainment |
| `hefaminc` | Household/family income category |
| `pemlr` | Labor-force status |
| `ptdtrace` | Race |
| `pwprmwgt` | Random-respondent survey weight |
| `pelaptop` | Laptop use |
| `pemphone` | Smartphone use |
| `peinhome` | Internet use at home |
| `peemail` | Email use |
| `pefinanc` | Internet use for financial services |
| `peegovts` | Online access to government services |
| `peedtrai` | Internet use for education or job training |

The raw source file remains unchanged.

This processed dataset can be recreated using:

`analysis/scripts/prepare_ntia_random_respondent_working.py`



### `openrepair_technology_working.csv`

Technology-focused working dataset derived from the Open Repair Alliance aggregate dataset.

- Source: Open Repair Data Standard (ORDS) v0.3 aggregate dataset
- Source period: data through July 2025
- Records retained: 47,024
- Variables retained: 12

Included product categories:

- Laptop
- Desktop computer
- Mobile
- Tablet
- Printer/scanner
- Flat screen
- Games console
- PC accessory
- Battery/charger/adapter
- TV and gaming-related accessories

Retained variables:

| Variable | Description |
|---|---|
| `id` | Repair record identifier |
| `data_provider` | Contributing repair organization |
| `country` | Country code |
| `product_category` | Standardized product category |
| `product_category_id` | Product category identifier |
| `brand` | Product brand |
| `year_of_manufacture` | Reported or estimated manufacture year |
| `product_age` | Reported or estimated product age |
| `repair_status` | Repair outcome |
| `repair_barrier_if_end_of_life` | Recorded barrier when item reached end of life |
| `event_date` | Repair event date |
| `problem` | Reported problem description |

The subset focuses on technology categories relevant to the capstone's device access, refurbishment, and reuse questions.

Product-age fields have substantial missingness and should not be treated as complete.

This processed dataset can be recreated using:

`analysis/scripts/prepare_openrepair_technology_working.py`
