-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.
-- not allowed to use join
SELECT * FROM hbtn_0d_usa WHERE name = 'California' ORDER BY cities.id DESC;
