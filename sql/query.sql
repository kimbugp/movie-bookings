WITH seats AS (
    SELECT DISTINCT
        s.id AS seat_id,
        st.id AS st_id
    FROM
        showtime st
    RIGHT JOIN seat s ON s.cinema_hall = st.cinema_hall
WHERE
    st.show_date_time > now()::date
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
    string_agg(DISTINCT seat.name || seat.number , ',') AS available_seats,
    st.id,
    m.name movie,
    st.price,
    st.show_date_time::varchar,
    c.name cinemahall
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
    st.id,
    movie,
    price,
    show_date_time,
    cinemahall
