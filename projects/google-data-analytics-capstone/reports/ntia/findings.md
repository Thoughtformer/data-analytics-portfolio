# NTIA 2023 Internet Use Survey — Findings

## Study Purpose

The NTIA 2023 Internet Use Survey was analyzed to identify patterns in technology use and digital engagement relevant to the proposed community technology initiative.

The analysis focused on differences associated with:

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

Reported household technology use rises substantially with household income.

Laptop use increases from:

- 41.2% among households earning under $25,000
- 84.6% among households earning $150,000 or more

This represents a 43.4 percentage-point difference.

Internet use at home also increases from:

- 71.0% among households earning under $25,000
- 90.3% among households earning $150,000 or more

**Analysis file:**  
`analysis/results/ntia_household_income_technology_use.csv`

---

### 2. Educational attainment shows a large technology-use gradient

Among adults age 25 and older, laptop use rises substantially with educational attainment:

- Less than high school: 21.4%
- High school / GED: 38.9%
- Some college / associate degree: 58.8%
- Bachelor's degree: 72.3%
- Graduate / professional degree: 77.3%

The difference between the lowest and highest education groups is 55.9 percentage points.

Internet use at home also rises from 63.1% among adults with less than a high school education to 87.2% among adults with a graduate or professional degree.

**Analysis file:**  
`analysis/results/ntia_education_technology_use.csv`

---

### 3. Educational attainment is also associated with digital engagement

Among adults age 25 and older, participation in several online activities rises with educational attainment.

From the lowest to highest education group:

- Email: 70.0% to 98.1%
- Online financial services: 49.4% to 88.5%
- Online government services: 19.5% to 55.8%
- Online education / job training: 7.1% to 34.1%

These measures represent reported online activity, not direct measures of digital literacy or proficiency.

**Analysis file:**  
`analysis/results/ntia_education_digital_engagement.csv`

---

### 4. Older, lower-income adults report particularly low technology use

Technology use differs by both age and household income.

Among adults in households earning under $25,000:

- Laptop use among ages 18–64: 40.7%
- Laptop use among ages 65+: 24.3%

Among adults age 65+ in households earning under $25,000:

- Laptop use: 24.3%
- Smartphone use: 58.3%
- Internet use at home: 55.9%

Within every income group analyzed, adults age 65+ report lower laptop, smartphone, and home-internet use than adults age 18–64.

**Analysis file:**  
`analysis/results/ntia_age_income_technology_use.csv`

---

### 5. Older, lower-income adults also report lower digital engagement

Among adults age 65+ in households earning under $25,000:

- Email: 74.1%
- Online financial services: 47.3%
- Online government services: 21.0%
- Online education / job training: 3.6%

Within every income group analyzed, adults age 65+ report lower participation in all four measured online activities than adults age 18–64.

This analysis is descriptive and does not establish a statistical interaction effect between age and income.

**Analysis file:**  
`analysis/results/ntia_age_income_digital_engagement.csv`

---

### 6. Youth technology use varies by household income

Among youth ages 3–17, reported technology use generally rises with household income.

From households earning under $25,000 to households earning $150,000 or more:

- Laptop use: 29.3% to 47.7%
- Tablet use: 24.5% to 45.7%
- Smartphone use: 33.0% to 44.0%
- Internet use at home: 62.5% to 74.2%

The largest observed differences are in laptop and tablet use.

**Analysis file:**  
`analysis/results/ntia_youth_income_technology_use.csv`

---

### 7. Texas is broadly similar to the United States on selected indicators

Texas adult estimates are close to national estimates across the selected technology-use and digital-engagement measures.

Observed differences between Texas and the national estimates are:

- Laptop use: -0.2 percentage points
- Smartphone use: +2.8 percentage points
- Internet use at home: +1.7 percentage points
- Online financial services: +1.9 percentage points
- Online government services: -0.4 percentage points

The NTIA data does not support characterizing Texas as having an unusually large statewide digital-use gap based on these measures.

The stronger disparities identified in this analysis occur within demographic and economic subgroups rather than between Texas and the United States overall.

**Analysis file:**  
`analysis/results/ntia_texas_vs_us.csv`

---

## Overall Interpretation

The NTIA analysis shows that technology use and digital engagement are not evenly distributed across the population.

The strongest disparities identified in this analysis are associated with:

1. Educational attainment
2. Household income
3. Older age combined with lower household income

Youth technology use also varies by household income.

These findings support further investigation of programs intended to improve technology access and digital support among lower-income households, older adults, and youth.

The NTIA evidence alone does not demonstrate that the proposed intervention will improve these outcomes. Evidence concerning device repairability, reusable technology supply, program feasibility, environmental impact, economic vulnerability, and intervention effectiveness must be evaluated separately.

---

## Tableau Visualization Candidates

The strongest candidates for the later Tableau visualization phase are:

- `ntia_household_income_technology_use.csv`
- `ntia_education_technology_use.csv`
- `ntia_age_income_technology_use.csv`
- `ntia_age_income_digital_engagement.csv`
- `ntia_education_digital_engagement.csv`
- `ntia_youth_income_technology_use.csv`
- `ntia_texas_vs_us.csv`

Not every analysis result needs to appear in the final Tableau story. Final visualizations should be selected based on relevance to the business task, clarity, and avoidance of redundant findings.

---

## Methodological Notes

- The analysis identifies associations, not causal relationships.
- Technology-use variables measure reported use rather than direct device ownership.
- Digital-engagement variables measure reported online activity rather than digital literacy or proficiency.
- Person-level technology estimates use the survey weight `PWSSWGT`.
- Random-respondent digital-engagement estimates use `PWPRMWGT`.
- Household-level estimates use `HWHHWGT`.
- Subgroup differences may reflect multiple overlapping demographic and economic factors.
