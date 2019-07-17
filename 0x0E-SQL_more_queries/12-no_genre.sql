-- Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- The database name will be passed as an argument of the mysql command

mysql -u root -p < hbtn_0d_tvshows.sql;
SELECT tv_shows.title, tv_show_genres.genre_id, FROM hbtn_0d_tvshow WHERE qty tv_show_genres = 1 GROUP BY tv_sho\
ws.title, tv_show_genres.genre_id ASC;
