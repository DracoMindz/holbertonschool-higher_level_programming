-- Import the database dump from hbtn_0d_tvshows to your MySQL server
-- Write a script that lists all shows contained in database that have at least one genre linked.
SELECT tv_shows.title, tv_show_genre.genre_id	FROM tv_shows JOIN tv_show_genres ON id = show.id ORDER BY title ASC, genre_id ASC;
