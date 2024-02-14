-- This script for 13-count_shows_by_genre.sql
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_shows
       FROM tv_show_genres
       INNER JOIN tv_genres
       ON tv_genres.id = tv_show_genres.genre_id
       GROUP BY tv_genres.name
       ORDER BY number_shows DESC;
