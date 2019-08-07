-- cte for seats , showtime ids, movie name and price
WITH seats AS (
    SELECT DISTINCT
        s.seat_number,
        st.id AS id,
        m.name movie,
        st.price,
        st.show_date_time::varchar,
        c.name cinemahall
    FROM
        showtime st
        --	right join seats to st to get all seats
    RIGHT JOIN seat s ON s.cinema_hall = st.cinema_hall
    --	join movie table with st table to get movie name
    INNER JOIN movie m ON m.id = st.movie_id
    --	join cinema table to get cinema name
    JOIN cinemahall c ON c.id = st.cinema_hall
    --	get only showtimes in the future
WHERE
    st.show_date_time > now()::date
EXCEPT
-- get seats which are already taken from tickets table
SELECT
    t.seat_number,
    t.showtime_id,
    NULL,
    NULL,
    NULL,
    NULL
FROM
    ticket t
)
