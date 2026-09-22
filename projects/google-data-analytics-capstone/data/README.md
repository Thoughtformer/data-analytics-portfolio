# Data

This folder documents the datasets used in the capstone project.

The project preserves a clear distinction between:

- **Raw source data** — original files obtained from public sources
- **Processed data** — cleaned, filtered, transformed, or analysis-ready datasets created during the project
- **Reference data** — supporting documentation, codebooks, or lookup material

## Primary Datasets

### P01 — NTIA Internet Use Survey

**Source:** National Telecommunications and Information Administration (NTIA)  
**Dataset:** 2023 Internet Use Survey  
**Status:** Acquired and analyzed

**Used to:**

- analyze technology and internet use
- compare device use across demographic groups
- evaluate digital engagement by age, income, and education
- identify measurable technology-access and support gaps

The analysis uses the appropriate survey weights for the working files and measures reported use rather than digital proficiency.

### P02 — Open Repair Alliance Data

**Source:** Open Repair Alliance  
**Dataset:** Open Repair Data  
**Status:** Acquired and analyzed

**Used to:**

- analyze repair outcomes
- filter to laptops, desktops, mobile phones, and tablets
- examine end-of-life records
- analyze documented barriers to successful repair
- evaluate device-reuse potential

Open Repair records are self-selected and are not treated as nationally representative.

### P03 — EPA Waste Reduction Model (WARM)

**Source:** U.S. Environmental Protection Agency (EPA)  
**Model:** Waste Reduction Model (WARM)  
**Status:** Used for scenario analysis

**Used to:**

- model greenhouse-gas effects for a defined 500-device portable-electronics scenario
- compare reuse/source reduction and recycling with landfill

The WARM results are modeled estimates, not observed program outcomes.

## Data Directory Structure

```text
data/
├── README.md
├── raw/
├── processed/
└── reference/
```

See the project source register and methodology log for detailed source and transformation documentation.
