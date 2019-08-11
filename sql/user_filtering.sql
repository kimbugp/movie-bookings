WITH user_tickets AS (
    SELECT DISTINCT
        users.id,
        users.email,
        users.name,
        array_agg(t.id) AS tickets,
        count(t) * st.price AS total,
        st.price
    FROM
        users
    LEFT JOIN ticket t ON t.user_id = users.id
    RIGHT JOIN showtime st ON st.id = t.showtime_id
WHERE
    t.id IS NOT NULL
    AND t.date_created BETWEEN '{ticket_startdate}'
    AND '{ticket_enddate}'
GROUP BY
    st.price,
    users.id
HAVING
    count(t) * st.price > {total}
)
SELECT
    id,
    email,
    sum(total) as total,
    user_tickets.name
FROM
    user_tickets
GROUP BY
    user_tickets.id,
    email,
    user_tickets.name
    --
