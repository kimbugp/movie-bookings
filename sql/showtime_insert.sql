WITH record AS (
{0}
)
SELECT
    record.id,
    show_date_time,
    json_agg(DISTINCT m) AS movie,
    json_agg(DISTINCT c) AS cinemahall,
    price
FROM
    record
    LEFT JOIN movie m ON m.id = record.movie_id
    LEFT JOIN cinemahall c ON c.id = record.cinema_hall
GROUP BY 
    record.id,
    show_date_time,
    price
