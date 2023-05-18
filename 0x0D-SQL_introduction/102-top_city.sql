-- script that displays the top 3 of cities temperature
-- during July and August ordered by temperature (descending)
SELECT city, temperature
FROM temperatures
WHERE month IN ('July', 'August')
ORDER BY temperature Desc
LIMIT 3;
