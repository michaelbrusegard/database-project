import sqlite3


def find_showings(date):
    connection = sqlite3.connect('trondelag_theatre.db')
    cursor = connection.cursor()
    
    query = """
    SELECT 
        p.name AS PlayName,
        s.time AS ShowTime,
        COALESCE(COUNT(t.showing_id), 0) AS TicketsSold
    FROM showings s
    JOIN plays p ON s.play_id = p.id
    LEFT JOIN tickets t ON s.id = t.showing_id
    WHERE s.time LIKE ?
    GROUP BY s.id
    ORDER BY s.time;
    """

    cursor.execute(query, (f'{date}%',))
    showings = cursor.fetchall()

    if showings:
        print(f"Showings on {date}:")
        for showing in showings:
            print(f"- {showing[0]} ({showing[1]}): {showing[2]} tickets sold.")
    else:
        print(f"No showings on {date}.")

    connection.close()

find_showings('2024-02-02')
find_showings('2024-02-03')
find_showings('2024-02-04')