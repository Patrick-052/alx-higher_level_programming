-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_shows
ON tv_genres.tv_shows_id = tv_shows.id
ORDER BY tv_genres.name Asc;
