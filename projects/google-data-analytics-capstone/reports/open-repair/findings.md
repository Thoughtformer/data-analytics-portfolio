# Open Repair Alliance Findings

## Purpose

This analysis examines whether community repair data supports the feasibility of refurbishing and extending the useful life of technology devices relevant to digital access.

The source is the Open Repair Alliance Open Repair Data Standard (ORDS) v0.3 aggregate dataset, containing repair-event records through July 2025.

A technology-focused working dataset was created containing 47,024 records across the following categories:

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

The dataset represents devices brought to participating repair events. It should not be treated as representative of all electronic devices, discarded electronics, or U.S. households.

---

## 1. Repair outcomes by technology category

Across every selected technology category, a majority of records resulted in either a completed repair or an assessment that the item remained repairable.

The highest combined fixed-or-repairable shares were:

- Mobile: 81.5%
- Laptop: 81.3%
- Desktop computer: 74.8%
- Tablet: 71.8%
- Games console: 70.8%
- PC accessory: 70.3%
- Battery/charger/adapter: 69.4%
- TV and gaming-related accessories: 64.0%
- Printer/scanner: 61.5%
- Flat screen: 58.7%

`Repairable` does not mean that the repair was completed. It means that reasonable next steps toward repair were identified.

### Interpretation

The results show that many technology devices brought to community repair events retain repair potential.

The findings support the feasibility of including device diagnosis and refurbishment in a community technology program, but they do not establish how many discarded devices in the general population would be recoverable.

---

## 2. Core digital-access devices

A narrower analysis focused on devices most directly relevant to digital access:

- Laptop
- Desktop computer
- Mobile
- Tablet

The subset contains 23,612 repair-event records.

Outcomes were:

- Fixed: 52.9%
- Repairable: 26.3%
- End of life: 17.1%
- Unknown: 3.7%
- Fixed or repairable: 79.2%

### Interpretation

Nearly four in five core access-device records were either successfully fixed or assessed as still repairable.

This provides evidence that community repair and refurbishment programs can recover a substantial share of devices that reach participating repair events.

It does not imply that 79.2% of all discarded computers, phones, or tablets are recoverable.

---

## 3. End-of-life barriers across technology devices

Among the selected technology categories, 11,560 records were classified as end of life.

A specific repair barrier was documented for 3,883 records, producing a barrier documentation rate of 33.6%.

Among records with a documented barrier:

- Repair information not available: 22.9%
- Spare parts not available: 18.9%
- Spare parts too expensive: 18.1%
- Item too worn out: 15.7%
- No way to open product: 12.6%
- Lack of equipment: 11.8%

### Interpretation

Most documented barriers were associated with repairability constraints such as information, parts, cost, equipment, or product accessibility rather than physical wear alone.

Because barrier information is missing for approximately two-thirds of end-of-life records, these percentages apply only to cases where a barrier was documented.

---

## 4. Barriers for core digital-access devices

Among laptops, desktops, mobiles, and tablets, 4,047 records were classified as end of life.

Barrier information was documented for 1,173 records, a documentation rate of 29.0%.

Among those documented barriers:

- Spare parts too expensive: 24.4%
- Repair information not available: 19.8%
- Spare parts not available: 16.1%
- Lack of equipment: 14.7%
- No way to open product: 13.1%
- Item too worn out: 11.9%

A combined 88.1% of documented barriers involved something other than the item simply being too worn out.

### Interpretation

For core access devices, repair failure frequently appears connected to resource or repairability constraints rather than physical deterioration alone.

This is relevant to a community repair model because some barriers may potentially be addressed through:

- access to tools and equipment
- technical training
- repair documentation
- parts sourcing
- parts harvesting from donor devices
- standardized repair procedures

The dataset does not establish how often these interventions would ultimately convert an end-of-life device into a successful repair.

---

## 5. Repair outcomes over time

Annual outcomes were examined from 2016 through 2024.

Years before 2016 were excluded because of low record counts. 2025 was excluded because the dataset contains only a partial year through July.

The fixed-or-repairable share changed from:

- 78.1% in 2016
- 73.6% in 2017
- 70.2% in 2018
- 70.4% in 2019
- 70.9% in 2020
- 72.1% in 2021
- 73.5% in 2022
- 72.2% in 2023
- 71.3% in 2024

The end-of-life share increased from 14.7% in 2016 to 26.5% in 2024.

### Interpretation

The dataset shows an observed increase in end-of-life outcomes over the period examined.

This should not be interpreted as evidence that electronic products generally became less repairable over time.

Changes may also reflect differences in:

- participating repair organizations
- countries represented
- product-category composition
- device age and condition
- reporting practices
- the types of devices brought to repair events

The time trend is therefore treated as a secondary descriptive finding.

---

## Geographic limitation

The Open Repair dataset is heavily influenced by European repair-event records.

The United States represents only a small portion of the technology subset.

The dataset is therefore useful primarily for understanding:

- observed repair-event outcomes
- repair barriers
- device repairability in community repair settings

It is not appropriate for estimating U.S. national repair rates or the prevalence of repairable electronic waste in the United States.

---

## Overall Open Repair finding

The Open Repair analysis provides evidence that a substantial share of technology devices presented at community repair events retain useful repair potential.

This is especially notable for devices directly related to digital access. Among laptops, desktops, mobile phones, and tablets, 79.2% of records were either fixed or assessed as repairable.

When core access devices did reach end of life and a barrier was documented, only 11.9% of barriers were attributed simply to the device being too worn out. The remainder involved factors such as parts cost, parts availability, repair information, tools, or product accessibility.

Taken together, these findings support the practical feasibility of device repair and refurbishment as one component of a broader community technology initiative.

They do not establish the number of devices that could be recovered locally, the cost per successful refurbishment, or the causal impact of such a program.

---

## Tableau candidates

The strongest Open Repair files for visualization are:

- `openrepair_category_outcomes.csv`
- `openrepair_core_access_device_outcomes.csv`
- `openrepair_core_access_device_barriers.csv`
- `openrepair_outcomes_by_year.csv`

The strongest likely headline visual is the repair-outcome comparison for core digital-access devices.
