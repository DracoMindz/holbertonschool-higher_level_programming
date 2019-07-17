-- Import in hbtn_0c_0 database this table dump
-- Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city, avg(value) AS 'avg temp' FROM tempuerature GROUP BY city ORDER BY avg temp DESC;
