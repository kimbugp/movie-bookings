WITH seats AS (
    SELECT DISTINCT
        s.id AS seat_id,
        st.id AS st_id
    FROM
        showtime st
    RIGHT JOIN seat s ON s.cinema_hall = st.cinema_hall
WHERE
    st.show_datetime > now()::date
    OR st.show_datetime > '{start_date}'
EXCEPT
DISTINCT
-- get seats which are already taken from tickets table
SELECT
    t.seat_id,
    t.showtime_id
FROM
    ticket t)
-- query to get showtime details field
SELECT
    json_agg(seat) AS available_seats,
    count(seat.id) AS number_of_seats,
    st.id,
    json_agg(DISTINCT m) AS movie,
    st.price,
    st.show_datetime::varchar,
    json_agg(DISTINCT c) AS cinemahall
FROM
    seats
    INNER JOIN showtime st ON st.id = seats.st_id
    --  join movie table with st table to get movie name
    INNER JOIN movie m ON m.id = st.movie_id
    -- join seats table to get the seat name
    JOIN seat ON seat.id = seats.seat_id
    --  join cinema table to get cinema name
    JOIN cinemahall c ON c.id = st.cinema_hall
    -- place holder for where clause
    {0}
GROUP BY
    st.id
