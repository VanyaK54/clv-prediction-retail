-- Total customers by country
SELECT Country, COUNT(*) AS TotalCustomers
FROM Customers
GROUP BY Country;

-- High value customers (CLV > 1000)
SELECT CustomerID, PredictedCLV
FROM CLVPredictions
WHERE PredictedCLV > 1000
ORDER BY PredictedCLV DESC;

-- Average CLV by Recency Bucket
SELECT
  CASE
    WHEN Recency <= 30 THEN '<1M'
    WHEN Recency <= 90 THEN '1-3M'
    WHEN Recency <= 180 THEN '3-6M'
    WHEN Recency <= 365 THEN '6-12M'
    ELSE '>1Y'
  END AS RecencyBucket,
  AVG(PredictedCLV) AS AvgCLV
FROM CLVPredictions
GROUP BY
  CASE
    WHEN Recency <= 30 THEN '<1M'
    WHEN Recency <= 90 THEN '1-3M'
    WHEN Recency <= 180 THEN '3-6M'
    WHEN Recency <= 365 THEN '6-12M'
    ELSE '>1Y'
  END;
