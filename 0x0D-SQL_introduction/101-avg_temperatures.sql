-- Import in hbtn_0c_0 database this table dump: download
-- script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY CITY
ORDER BY avg_temp Desc;
