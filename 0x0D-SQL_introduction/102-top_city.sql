-- script that displays the top 3 of cities temperature
-- during July and August ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month IN ('July', 'August')
GROUP BY CITY
ORDER BY avg_temp Desc
LIMIT 3;
