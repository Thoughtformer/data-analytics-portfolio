# Closing the Digital Support Gap
## Evaluating a Community Technology Pilot Through Public Data

**Google Data Analytics Professional Certificate — Capstone Project**

## Project Status

Complete

## Project Overview

This capstone evaluates whether public evidence supports a limited community technology pilot centered on three components:

- device refurbishment and reuse
- hands-on technical training
- personalized digital support

Older adults are treated as a priority population because the analysis identifies lower levels of internet-based financial-services use among adults age 65+ across the income groups examined.

The analysis combines national technology-use data, community repair records, environmental scenario modeling, SQL validation, Python analysis, and Tableau visualization. The goal is not to claim that a full-scale program is already proven, but to determine whether the available evidence is strong enough to justify a limited, measurement-focused pilot.

## Decision Question

**Should a community organization, municipality, library system, foundation, or nonprofit fund a limited community technology pilot?**

The decision standard is whether the evidence demonstrates enough measurable need, repair potential, and public benefit to justify testing the model before broader implementation.

## Key Findings

- **43.4 percentage-point laptop-use gap by household income.** Weighted National Telecommunications and Information Administration (NTIA) 2023 data show laptop use rising from **41.2%** among households earning under $25,000 to **84.6%** among households earning $150,000 or more.
- **Older adults report lower internet-based financial-services use.** Overall use was **63.2% among adults age 65+** versus **81.6% among adults ages 18–64**, with the gap persisting across the household-income groups analyzed.
- **79.2% of core-device repair records were fixed or remained repairable.** Of 23,612 laptop, desktop, mobile-phone, and tablet repair records, **52.9% were fixed** and **26.3% were classified as repairable**.
- **Most documented end-of-life barriers were not simple wear-out.** Among end-of-life records with a documented barrier, **88.1%** involved parts cost or availability, repair information, equipment, or product access rather than the item simply being too worn out.
- **Reuse showed a substantial modeled environmental co-benefit.** An EPA Waste Reduction Model (WARM) scenario for **500 portable electronic devices** estimated **41.13 metric tons of carbon dioxide equivalent (MTCO2e)** avoided through reuse/source reduction versus landfill, compared with **1.49 MTCO2e** for recycling versus landfill.

## Recommendation

The evidence supports funding a **limited, measurement-focused pilot** combining device refurbishment and reuse, hands-on technical training, and personalized digital support.

The pilot should be evaluated before considering broader implementation.

## Data Sources

### NTIA 2023 Internet Use Survey
Used to analyze technology use and internet-based activity by household income, age, education, and geography. Survey weights were used in the analysis.

### Open Repair Alliance — Open Repair Data
Used to analyze repair outcomes and documented barriers for laptops, desktops, mobile phones, and tablets.

### U.S. Environmental Protection Agency — Waste Reduction Model (WARM)
Used for a defined environmental scenario comparing reuse/source reduction and recycling with landfill for portable electronic devices.

Additional public research and comparable-program evidence were manually reviewed and documented in the project source register and supporting reports.

## Analysis Workflow

The project follows the Google data analysis process:

1. **Ask** — define the decision question and evidence standard.
2. **Prepare** — identify, evaluate, and document relevant public datasets and external evidence.
3. **Process** — clean and reshape source data into analysis-ready working files.
4. **Analyze** — use Python and SQL to calculate weighted technology-use measures, repair outcomes, repair barriers, and environmental scenarios.
5. **Share** — build Tableau visualizations and a final presentation.
6. **Act** — translate the findings into a limited pilot recommendation with explicit measurement requirements.

## Tools

- **Python**
- **pandas**
- **SQL**
- **Google BigQuery**
- **Tableau Desktop Public Edition**
- **Microsoft PowerPoint**
- **Git / GitHub**

## SQL Validation

Key analytical findings were independently reproduced in BigQuery using SQL, including:

- NTIA household technology use by income
- Open Repair core-device repair outcomes
- Open Repair end-of-life repair barriers

SQL queries are stored in [`analysis/SQL/`](analysis/SQL/), and validated output files are stored in [`analysis/results/`](analysis/results/).

## Project Structure

```text
google-data-analytics-capstone/
├── README.md
├── analysis/
│   ├── SQL/
│   ├── results/
│   └── scripts/
├── data/
│   ├── processed/
│   ├── raw/
│   └── reference/
├── docs/
│   ├── methodology-log.md
│   ├── ntia-findings-summary.md
│   ├── project-charter.md
│   ├── research-plan.md
│   └── source-register.md
└── reports/
    ├── comparable-programs/
    ├── ntia/
    ├── open-repair/
    ├── supporting-evidence/
    ├── tableau/
    ├── evidence-synthesis.md
    ├── recommendation-framework.md
    ├── google-data-analytics-capstone-presentation.pdf
    └── google-data-analytics-capstone-presentation.pptx
```

## Selected Deliverables

- **[Final presentation — PDF](reports/google-data-analytics-capstone-presentation.pdf)**
- **[Final presentation — PowerPoint](reports/google-data-analytics-capstone-presentation.pptx)**
- [`reports/tableau/`](reports/tableau/) — Tableau workbook and visualization documentation
- [`analysis/results/`](analysis/results/) — analysis outputs and validated result tables
- [`analysis/SQL/`](analysis/SQL/) — BigQuery validation queries
- [`analysis/scripts/`](analysis/scripts/) — Python analysis scripts
- [`reports/evidence-synthesis.md`](reports/evidence-synthesis.md) — integrated evidence review
- [`reports/recommendation-framework.md`](reports/recommendation-framework.md) — decision and pilot framework

## Limitations

- NTIA measures reported technology and internet use, not digital proficiency.
- Open Repair data are self-selected and are not nationally representative.
- Repair-barrier information was documented for only **29.0%** of core-device end-of-life records.
- The WARM result is a modeled scenario, not an observed program outcome.
- The findings support testing a limited pilot; they do not establish the effectiveness of a full-scale integrated program.

## AI-Assisted Workflow

Artificial intelligence tools assisted with source discovery, code drafting, workflow planning, summarization, and documentation. External sources and analytical outputs were manually reviewed and validated. Final decisions regarding data selection, methodology, interpretation, limitations, and recommendations were made by the analyst.
