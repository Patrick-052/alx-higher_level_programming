-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.tv_shows_id
ORDER BY v_shows.title ASC, tv_show_genres.genre_id ASC;
