-- script that creates the table force_name on your MySQL server
-- database name will be passed as an argument, if table exists script should not fail
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
