-- script that displays the max temperature of each state 
-- requires the use of max(value)
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state ASC;
