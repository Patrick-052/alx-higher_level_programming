-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT genre, COUNT(tv_shows.id) AS number_of_shows
FROM tv_show_genres
INNER JOIN tv_shows
ON tv_shows.id = tv_show_genres.tv_show_id
GROUP BY genre
ORDER BY number_of_shows DESC;
