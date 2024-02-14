-- this script for 102-rating_shows.sql
SELECT tv_shows.title, SUM(hbtn_0d_tvshows_rate.rating) AS rating_sum
FROM tv_shows
JOIN hbtn_0d_tvshows_rate ON tv_shows.id = hbtn_0d_tvshows_rate.show_id
GROUP BY tv_shows.id, tv_shows.title
ORDER BY rating_sum DESC;
