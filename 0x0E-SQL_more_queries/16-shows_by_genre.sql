-- Lists all shows and all genres linkedd to that show from the database
SELECT tv_shows.title, tv_genres.name FROM tv_shows LEFT JOIN tv_
show_genres ON tv_shows.id = tv_show_genres.show_id LEFT JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id ORDER BY tv_shows.title ASC, t
v_genres.name ASC;
