-- a script that converts hbtn_0c_0 database to UTF8 (
-- converting from table first_table, field name
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table  CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; 
