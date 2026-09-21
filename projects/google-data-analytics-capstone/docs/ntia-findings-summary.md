# NTIA 2023 Internet Use Survey — Findings Summary

## Purpose

The NTIA 2023 Internet Use Survey was analyzed to evaluate patterns in technology use and digital engagement that may support the need for a community technology access, education, repair, and support initiative.

The analysis focused primarily on differences associated with:

- Age
- Household income
- Educational attainment
- Youth technology use
- Older adults
- Texas compared with national estimates

All findings are descriptive and should not be interpreted as evidence of causation.

---

## Key Findings

### 1. Household income is strongly associated with technology use

Household laptop use rises substantially across income groups:

- Under $25,000: 41.2%
- $150,000+: 84.6%

This represents a 43.4 percentage-point difference.

Household internet use at home also rises from 71.0% among households earning under $25,000 to 90.3% among households earning $150,000 or more.

Source:

`analysis/results/ntia_household_income_technology_use.csv`

---

### 2. Educational attainment shows one of the strongest technology-use gradients

Among adults age 25 and older, laptop use rises from:

- Less than high school: 21.4%
- Graduate / professional degree: 77.3%

This represents a 55.9 percentage-point difference.

Source:

`analysis/results/ntia_education_technology_use.csv`

---

### 3. Educational attainment is also strongly associated with digital engagement

Among adults age 25 and older, online financial-service use rises from:

- Less than high school: 49.4%
- Graduate / professional degree: 88.5%

Online government-service use rises from:

- Less than high school: 19.5%
- Graduate / professional degree: 55.8%

Source:

`analysis/results/ntia_education_digital_engagement.csv`

---

### 4. Older, lower-income adults show particularly low technology use

Among adults in households earning under $25,000:

- Ages 18–64 laptop use: 40.7%
- Ages 65+ laptop use: 24.3%

For adults age 65+ earning under $25,000:

- Smartphone use: 58.3%
- Internet use at home: 55.9%

Source:

`analysis/results/ntia_age_income_technology_use.csv`

---

### 5. Older, lower-income adults also show lower digital engagement

Among adults age 65+ in households earning under $25,000:

- Email: 74.1%
- Online financial services: 47.3%
- Online government services: 21.0%
- Online education / job training: 3.6%

Within every income group analyzed, adults age 65+ report lower participation in the measured online activities than adults age 18–64.

Source:

`analysis/results/ntia_age_income_digital_engagement.csv`

---

### 6. Youth technology use also varies by household income

Among youth ages 3–17, reported technology use generally rises with household income.

From households earning under $25,000 to households earning $150,000 or more:

- Laptop use: 29.3% to 47.7%
- Tablet use: 24.5% to 45.7%
- Smartphone use: 33.0% to 44.0%
- Internet use at home: 62.5% to 74.2%

Source:

`analysis/results/ntia_youth_income_technology_use.csv`

---

### 7. Texas is broadly similar to the national population on selected indicators

Texas adult estimates are close to national estimates for the selected technology-use and digital-engagement measures.

Observed Texas differences from national estimates range from:

- -0.4 percentage points for online government services
- to +2.8 percentage points for smartphone use

The NTIA data therefore does not support characterizing Texas as having an unusually large statewide digital-use gap based on these measures.

The stronger disparities appear within demographic and economic subgroups rather than between Texas and the United States overall.

Source:

`analysis/results/ntia_texas_vs_us.csv`

---

## Overall Interpretation

The NTIA analysis provides evidence that technology use and digital engagement are not evenly distributed across the population.

The strongest disparities are associated with:

1. Educational attainment
2. Household income
3. Age combined with lower household income

The results support further investigation of programs aimed at improving technology access and digital support among lower-income households, older adults, and youth.

The NTIA findings alone do not demonstrate that a specific intervention will improve these outcomes. Evidence about repairability, program feasibility, environmental impact, fraud vulnerability, and intervention effectiveness must be evaluated separately.

---

## Tableau Visualization Shortlist

The following result files are the strongest candidates for later Tableau visualization:

1. `ntia_household_income_technology_use.csv`
   - Household income versus laptop, tablet, mobile-phone, and home-internet use

2. `ntia_education_technology_use.csv`
   - Educational attainment versus technology use

3. `ntia_age_income_technology_use.csv`
   - Age and income combined versus technology use

4. `ntia_age_income_digital_engagement.csv`
   - Age and income combined versus online activity

5. `ntia_education_digital_engagement.csv`
   - Educational attainment versus online activity

6. `ntia_youth_income_technology_use.csv`
   - Youth technology use by household income

7. `ntia_texas_vs_us.csv`
   - Texas versus national comparison

Not every result file must appear in the final Tableau story. Final visualizations should be selected based on clarity, relevance to the business task, and avoidance of redundant findings.

---

## Methodological Limitations

- Survey results identify associations, not causal relationships.
- Technology-use variables measure reported use rather than direct device ownership.
- Digital-engagement variables measure reported online activity rather than digital literacy or proficiency.
- Survey weights must be applied according to the question universe.
- Person-level estimates use `PWSSWGT`.
- Random-respondent estimates use `PWPRMWGT`.
- Household-level estimates use `HWHHWGT`.
- Subgroup comparisons may reflect multiple overlapping demographic and economic factors.
