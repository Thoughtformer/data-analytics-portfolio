SELECT
  COUNT(*) AS total_records,

  SUM(CASE WHEN repair_status = 'Fixed' THEN 1 ELSE 0 END) AS fixed_count,

  SUM(CASE WHEN repair_status = 'Repairable' THEN 1 ELSE 0 END) AS repairable_count,

  SUM(CASE WHEN repair_status = 'End of life' THEN 1 ELSE 0 END) AS end_of_life_count,

  SUM(CASE WHEN repair_status = 'Unknown' THEN 1 ELSE 0 END) AS unknown_count,

  SUM(
    CASE
      WHEN repair_status IN ('Fixed', 'Repairable') THEN 1
      ELSE 0
    END
  ) AS fixed_or_repairable_count,

  ROUND(
    SUM(
      CASE
        WHEN repair_status IN ('Fixed', 'Repairable') THEN 1
        ELSE 0
      END
    ) * 100.0 / COUNT(*),
    1
  ) AS fixed_or_repairable_pct

FROM
  `data-analytics-capstone-509318.capstone_analysis.openrepair_technology`

WHERE
  product_category IN ('Laptop', 'Desktop computer', 'Mobile', 'Tablet');