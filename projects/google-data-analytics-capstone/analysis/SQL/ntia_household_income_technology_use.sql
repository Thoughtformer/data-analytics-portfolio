SELECT
  CASE
    WHEN hefaminc BETWEEN 1 AND 7 THEN 'Under $25,000'
    WHEN hefaminc BETWEEN 8 AND 11 THEN '$25,000-$49,999'
    WHEN hefaminc BETWEEN 12 AND 13 THEN '$50,000-$74,999'
    WHEN hefaminc = 14 THEN '$75,000-$99,999'
    WHEN hefaminc = 15 THEN '$100,000-$149,999'
    WHEN hefaminc = 16 THEN '$150,000+'
  END AS income_group,

  ROUND(
    SUM(CASE WHEN helaptop = 1 THEN hwhhwgt ELSE 0 END)
    / SUM(CASE WHEN helaptop IN (1, 2) THEN hwhhwgt ELSE 0 END)
    * 100,
    1
  ) AS laptop_use_pct,

  ROUND(
    SUM(CASE WHEN hedesktp = 1 THEN hwhhwgt ELSE 0 END)
    / SUM(CASE WHEN hedesktp IN (1, 2) THEN hwhhwgt ELSE 0 END)
    * 100,
    1
  ) AS desktop_use_pct,

  ROUND(
    SUM(CASE WHEN hetablet = 1 THEN hwhhwgt ELSE 0 END)
    / SUM(CASE WHEN hetablet IN (1, 2) THEN hwhhwgt ELSE 0 END)
    * 100,
    1
  ) AS tablet_use_pct,

  ROUND(
    SUM(CASE WHEN hemphone = 1 THEN hwhhwgt ELSE 0 END)
    / SUM(CASE WHEN hemphone IN (1, 2) THEN hwhhwgt ELSE 0 END)
    * 100,
    1
  ) AS mobile_use_pct,

  ROUND(
    SUM(CASE WHEN heinhome = 1 THEN hwhhwgt ELSE 0 END)
    / SUM(CASE WHEN heinhome IN (1, 2) THEN hwhhwgt ELSE 0 END)
    * 100,
    1
  ) AS home_internet_use_pct

FROM
  `data-analytics-capstone-509318.capstone_analysis.ntia_2023_household`

WHERE
  hefaminc BETWEEN 1 AND 16

GROUP BY
  income_group

ORDER BY
  MIN(hefaminc);