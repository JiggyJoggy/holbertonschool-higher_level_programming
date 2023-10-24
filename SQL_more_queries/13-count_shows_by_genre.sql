-- Lists all genres from hbtn_0d_tvshows
-- and displays the number of shows linked to each
SELECT tv_genres.name AS 'genre'
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;