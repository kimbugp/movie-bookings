SELECT
    TRUE AS result
WHERE
    '{0}' IN ( SELECT DISTINCT
            seat_number
        FROM
            showtime st
        RIGHT JOIN seat s ON s.cinema_hall = st.cinema_hall
    WHERE
        st.id = {1}
    EXCEPT
    SELECT
        t.seat_number
    FROM
        ticket t
    WHERE
        t.showtime_id = {1})
