SELECT
  repair_barrier_if_end_of_life,
  COUNT(*) AS barrier_count,
  ROUND(
    COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (),
    1
  ) AS barrier_pct
FROM
  `data-analytics-capstone-509318.capstone_analysis.openrepair_technology`
WHERE
  product_category IN ('Laptop', 'Desktop computer', 'Mobile', 'Tablet')
  AND repair_status = 'End of life'
  AND repair_barrier_if_end_of_life IS NOT NULL
GROUP BY
  repair_barrier_if_end_of_life
ORDER BY
  barrier_count DESC;