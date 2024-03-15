import sqlite3

connection = sqlite3.connect('trondelag_theatre.db')
cursor = connection.cursor()

def find_showings(date):
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
    results = cursor.fetchall()

    if results:
        print(f"Showings on {date}:")
        for result in results:
            print(f"- {result[0]} ({result[1]}): {result[2]} tickets sold.")
    else:
        print(f"No showings on {date}.")

find_showings('2024-02-02')
find_showings('2024-02-03')
find_showings('2024-02-04')

connection.close()