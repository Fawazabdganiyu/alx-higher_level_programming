-- List all genres contained in the database `hbtn_0d_tvshows`
-- and display the number of shows linked to each.
SELECT tg.name AS genre, COUNT(tsg.show_id) AS number_of_shows
  FROM tv_genres AS tg
       INNER JOIN tv_show_genres AS tsg
       ON tg.id = tsg.genre_id
 GROUP BY genre
 ORDER BY number_of_shows DESC;
