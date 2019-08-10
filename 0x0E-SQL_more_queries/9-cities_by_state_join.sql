-- script that lists all cities contained in the database hbtn_0d_usa
-- results must be sorted in ascending order
SELECT cities.id, cities.name, states.name FROM cities JOIN states on states.id = cities.state_id ORDER BY cities.id ASC; 
