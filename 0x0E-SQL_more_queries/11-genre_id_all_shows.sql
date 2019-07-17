-- Import the database dump of hbtn_0d_tvshows to your MySQL server: download 
-- Write a script that lists all shows contained in the database hbtn_0d_tvshows.
SELECT name AS genre, COUNT (*) AS number_of_shows FROM tv_genres GROUP BY genre FROM tv_show_genre JOIN ON genre_id = id GROUP BY genre ORDER BY number_of_shows DESC;
