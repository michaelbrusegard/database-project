import sqlite3
def sort_by_selling():
    connection = sqlite3.connect('trondelag_theatre.db')
    cursor = connection.cursor()

    sql_query = """
    SELECT 
        tickets.showing_id, 
        showings.id, 
        showings.time, 
        showings.play_id, 
        plays.id, 
        plays.name,
        COUNT(*) AS tickets_sold
    FROM 
        tickets
    JOIN 
        showings ON tickets.showing_id = showings.id
    JOIN 
        plays ON showings.play_id = plays.id
    GROUP BY 
        showings.id
    ORDER BY 
        tickets_sold DESC;
    """
    cursor.execute(sql_query)
    showing = cursor.fetchall()
    for show in showing:
        print(f"- {show[5]} - Date: {show[2]} - Tickets sold: {show[6]}")
    connection.close()
sort_by_selling()