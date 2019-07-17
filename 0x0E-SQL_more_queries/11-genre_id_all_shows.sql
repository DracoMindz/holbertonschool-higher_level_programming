-- Import the database dump of hbtn_0d_tvshows to your MySQL server: download 
-- Write a script that lists all shows contained in the database hbtn_0d_tvshows.
mysql -u root -p < hbtn_0d_tvshows.sql;
SELECT tv_shows.title, tv_show_genres.genre_id, FROM hbtn_0d_tvshow WHERE qty tv_show_genres = 1 GROUP BY tv_sho\
ws.title, tv_show_genres.genre_id ASC;
