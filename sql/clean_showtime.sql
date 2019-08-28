SELECT
    st.id,
    st.show_datetime,
    m.name,
    m.length,
    st.show_datetime + m.length endtime,
    st.cinema_hall
FROM
    showtime st
    INNER JOIN movie m ON m.id = movie_id
WHERE
    cinema_hall = {cinema_hall}
    AND movie_id = {movie_id}
    AND '{show_datetime}' BETWEEN st.show_datetime
    AND st.show_datetime + m.length
