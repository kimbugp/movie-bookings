--Check if  seat is available for a showtime
SELECT
    TRUE AS result
WHERE
    {seat_id} IN ( SELECT DISTINCT
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
        t.showtime_id = {showtime_id})

