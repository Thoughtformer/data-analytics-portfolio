# Source & Evidence Register

This document tracks the datasets, institutional reports, and external evidence used in the capstone project.

Sources are classified as:

- **Primary datasets** — data that will be directly cleaned, queried, analyzed, or visualized.
- **Supporting sources** — published data, research, reports, or program evaluations used to provide context, validate findings, or evaluate intervention feasibility.

---

## Primary Analytical Datasets

| ID | Source | Dataset | Year / Version | Scope | Project Role | Status |
|---|---|---|---|---|---|---|
| P01 | [National Telecommunications and Information Administration (NTIA)](https://www.ntia.gov/page/download-ntia-internet-use-survey-datasets) | Internet Use Survey | 2023 | United States; approximately 44,000 interviewed households; person-level questions for household members age 3+ | Analyze internet access, device use, digital participation, and demographic differences | To acquire |
| P02 | [Open Repair Alliance](https://openrepair.org/open-data/downloads/) | Open Repair Data | ORDS v0.3; data through July 2025 | International; 305,649 electrical and electronic repair attempts | Analyze repair outcomes, product categories, product age, and barriers to successful repair | To acquire |

---

## Supporting Data & Evidence

### Digital Access and Skills

| ID | Source | Dataset / Report | Year | Population / Coverage | Project Role |
|---|---|---|---|---|---|
| S01 | [U.S. Census Bureau](https://data.census.gov/table/ACSST1Y2024.S2802) | ACS Table S2802 — Types of Internet Subscriptions by Selected Characteristics | 2024 | United States; American Community Survey population estimates | Compare broadband and computer access across demographic groups |
| S02 | [National Center for Education Statistics (NCES)](https://nces.ed.gov/surveys/piaac/2023/national_results.asp) | PIAAC U.S. National Results | 2023 | U.S. adults ages 16–74; 4,637 background-questionnaire respondents and 4,574 assessment respondents | Examine adaptive problem-solving proficiency by age, education, and employment |
| S03 | [National Center for Education Statistics (NCES)](https://nces.ed.gov/programs/digest/d25/tables/dt25_702.12.asp) | Digest Table 702.12 — Children's Home Internet and Device Access | 2022–2023 | U.S. children ages 3–18 living in households | Examine computer access, smartphone-only access, and socioeconomic differences among youth |

---

### Economic Vulnerability and Fraud

| ID | Source | Dataset / Report | Year | Population / Coverage | Project Role |
|---|---|---|---|---|---|
| S04 | [Federal Trade Commission (FTC)](https://www.ftc.gov/reports/consumer-sentinel-network-data-book-2024) | Consumer Sentinel Network Data Book | 2024 | Approximately 6.5 million consumer reports received during 2024 | Examine reported fraud losses, age differences, and scam categories |
| S05 | [FBI Internet Crime Complaint Center (IC3)](https://www.ic3.gov/AnnualReport/Reports) | Annual Internet Crime Reports | Annual series; through 2025 | United States; complaints submitted to IC3 | Examine reported cybercrime and fraud losses affecting older adults |

---

### Environmental Impact and Electronic Waste

| ID | Source | Dataset / Report | Year / Version | Coverage | Project Role |
|---|---|---|---|---|---|
| S06 | [U.S. Environmental Protection Agency (EPA)](https://www.epa.gov/electronics-batteries-management/assessment-tools-electronics-stewardship) | Electronics Stewardship Assessment Tools | Current tool versions to be recorded during analysis | United States | Estimate environmental effects associated with electronics reuse, recycling, and extended device life |
| S07 | [International Telecommunication Union (ITU) / UNITAR](https://www.itu.int/en/ITU-D/Environment/Pages/Publications/The-Global-E-waste-Monitor-2024.aspx) | Global E-waste Monitor | 2024 report; reference data year 2022 | Global | Provide context for electronic-waste generation, collection, and recycling |

---

### Comparable Programs and Intervention Evidence

| ID | Source | Program / Evaluation | Period | Coverage | Project Role |
|---|---|---|---|---|---|
| S08 | [Government of Canada](https://www.ised-isde.canada.ca/site/audits-evaluations/en/evaluation/evaluation-computers-schools-plus-cfs-and-computer-schools-intern-cfsi-programs) | Evaluation of Computers for Schools Plus and Computers for Schools Intern Programs | 2016–2022; published 2023 | Canada | Evaluate evidence from a large-scale device refurbishment, distribution, and youth-training model |
| S09 | [City of Los Angeles](https://ita.lacity.gov/news/ourcycle-la) | OurCycle LA | Program reporting | Los Angeles, California | Examine a U.S. model combining device refurbishment, youth technical training, digital literacy, and computer distribution |
| S10 | [Open Repair Alliance](https://openrepair.org/open-data/insights/) | Community Repair Research and Insights | Multiple reports | International repair-community data | Provide published context for repair outcomes and common repair barriers |

---

## Methodology & Known Limitations

| ID | Methodology / Data Source | Known Limitations |
|---|---|---|
| P01 | Supplement to the U.S. Census Bureau Current Population Survey; household and person-level responses; consistency editing and imputation are used for eligible missing responses | Survey and proxy-response data; estimates require appropriate weighting; some responses are imputed; cross-sectional relationships do not establish causation |
| P02 | Repair-event records contributed by Open Repair Alliance partner organizations | Devices and participants are self-selected; results are not representative of all discarded electronics or all households |
| S01 | American Community Survey probability sample with weighted population estimates | Estimates include sampling error and margins of error; aggregate relationships do not establish individual-level causation |
| S02 | Nationally representative adult skills assessment using a background questionnaire and tablet-based assessment | Survey weighting is required; U.S. response rates were relatively low; associations do not establish causation |
| S03 | Published national estimates of youth internet and device access | Aggregate estimates rather than individual-level project data; relationships should not be interpreted as causal |
| S04 | Consumer reports submitted directly to the FTC and through participating organizations | Reports are self-reported and unverified; Consumer Sentinel is not a population survey and cannot directly estimate fraud prevalence |
| S05 | Complaints submitted to the FBI Internet Crime Complaint Center | Complaint data represent reported incidents only; underreporting and differences in reporting behavior may affect observed patterns |
| S06 | Model-based environmental assessment tools including the Electronics Environmental Benefits Calculator and WARM | Results depend on model assumptions and user inputs; modeled estimates must be distinguished from observed outcomes |
| S07 | International statistical reporting and modeling | Data quality and reporting consistency vary across countries; global findings should not be treated as direct estimates of local community conditions |
| S08 | Government program evaluation using multiple qualitative and quantitative sources | Program evaluation rather than randomized experimental research; documentation identifies gaps in some performance measures |
| S09 | City program administrative reporting | Reported accomplishments are not equivalent to an independent impact evaluation and do not establish causation |
| S10 | Published analyses from the same Open Repair ecosystem as P02 | Some findings may rely on data overlapping with P02 and should not be treated as fully independent confirmation |

---

## Access & Licensing Notes

| ID | Access / Format | Licensing / Attribution |
|---|---|---|
| P01 | Public-use files available in CSV, R, Stata, and fixed-width formats | Source attribution required; specific reuse terms to be reviewed before republishing raw files |
| P02 | Public downloadable repair dataset | Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) |
| S01 | Public Census data tables and downloads | U.S. Census Bureau source attribution |
| S02 | Public NCES reports and statistical tables | NCES source attribution |
| S03 | Public NCES statistical table | NCES source attribution |
| S04 | Published report, dashboards, and downloadable CSV data | FTC source attribution |
| S05 | Published FBI IC3 reports | FBI / IC3 source attribution |
| S06 | Public EPA calculators and methodology resources | EPA source attribution; tool version should be recorded when used |
| S07 | Published international report and supporting data | ITU / UNITAR source attribution |
| S08 | Public Government of Canada evaluation | Government of Canada source attribution |
| S09 | Public City of Los Angeles program reporting | City of Los Angeles source attribution |
| S10 | Public Open Repair Alliance research and insights | Open Repair Alliance attribution; applicable source licenses should be reviewed |

---

## Source Status Definitions

| Status | Meaning |
|---|---|
| **Identified** | Source has been located and determined to be potentially relevant |
| **To acquire** | Dataset has been selected but has not yet been downloaded or imported |
| **Acquired** | Original dataset has been obtained and preserved |
| **Reviewed** | Documentation, structure, methodology, and variables have been examined |
| **In analysis** | Source is actively being cleaned, queried, analyzed, or visualized |
| **Complete** | Relevant analysis and documentation have been completed |

---

## Metadata Still to Finalize

The following information will be added as each source is actively used:

- Exact variables and metrics selected
- Date accessed
- Local dataset filename and version
- Imported row and column counts
- Cleaning and transformation steps
- Project files using each source
- Figures or tables derived from each source
- Exact tool versions where applicable
- Additional limitations discovered during analysis
- Final citation format
