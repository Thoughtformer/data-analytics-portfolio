# SQL Analysis

Selected headline findings from this capstone are independently reproduced and validated in Google BigQuery using Structured Query Language (SQL).

## BigQuery Environment

- Google Cloud project: `data-analytics-capstone-509318`
- BigQuery dataset: `capstone_analysis`
- Current table: `openrepair_technology`

Additional processed datasets may be loaded into the same BigQuery dataset as needed for validation.

## Purpose

SQL is used to demonstrate and validate:

- filtering
- grouping
- aggregation
- conditional aggregation
- percentage calculations
- weighted survey calculations

Python was used primarily for data preparation, exploratory analysis, reproducible processing, and initial result generation.

The SQL analyses serve as independent validation of selected findings rather than a complete reimplementation of every Python analysis.

## File Organization

Each meaningful SQL analysis is saved as its own `.sql` file in this folder.

Corresponding exported query results are saved in:

`projects/google-data-analytics-capstone/analysis/results/`

SQL-generated result files use the suffix `_sql.csv` to distinguish them from Python-generated outputs.

## Current SQL Scope

Planned validation includes:

- Open Repair category outcomes
- Open Repair core access-device outcomes
- Open Repair end-of-life barrier frequencies
- National Telecommunications and Information Administration (NTIA) weighted household technology-use calculations

The SQL work is intentionally focused on validating major findings used in the final capstone rather than reproducing every exploratory analysis.
