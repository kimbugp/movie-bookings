--Check if  seat is available for a showtime
WITH seats AS (
    SELECT DISTINCT
        s.id
    FROM
        showtime st
    RIGHT JOIN seat s ON s.cinema_hall = st.cinema_hall
WHERE
    st.id = {showtime_id}
EXCEPT
-- select seats which are occupied
SELECT
    t.seat_id
FROM
    ticket t
WHERE
    t.showtime_id = {showtime_id}
)
SELECT
    array_agg(seats.id)
FROM
    seats
