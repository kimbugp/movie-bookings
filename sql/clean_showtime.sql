SELECT
    st.id,
    st.show_date_time,
    m.name,
    m.length,
    st.show_date_time + m.length endtime,
    st.cinema_hall
FROM
    showtime st
    INNER JOIN movie m ON m.id = movie_id
WHERE
    cinema_hall = {cinema_hall}
    AND movie_id = {movie_id}
    AND '{show_date_time}' BETWEEN st.show_date_time
    AND st.show_date_time + m.length
