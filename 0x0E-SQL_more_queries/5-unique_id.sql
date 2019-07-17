-- script that creates the table unique_id on your MySQL server.
-- id with default unique value
CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));

