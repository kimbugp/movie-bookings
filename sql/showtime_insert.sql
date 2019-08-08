WITH record AS (
{0}
)
SELECT
    record.id,
    show_date_time,
    m.name movie,
    c.name cinemahall,
    price
FROM
    record
    LEFT JOIN movie m ON m.id = record.movie_id
    LEFT JOIN cinemahall c ON c.id = record.cinema_hall
