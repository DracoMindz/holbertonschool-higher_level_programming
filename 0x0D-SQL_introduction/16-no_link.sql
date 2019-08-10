-- script that lists all records of the table 
-- rows must have name value, descending, (score, name)
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;     
