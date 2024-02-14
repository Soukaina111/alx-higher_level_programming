-- This script for  13-count_shows_by_genre.sql
SELECT tv_show_genres.genre_id AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_show_genres GROUP BY tv_show_genres.genre_id HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
