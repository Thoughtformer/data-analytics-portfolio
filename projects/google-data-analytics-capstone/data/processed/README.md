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
