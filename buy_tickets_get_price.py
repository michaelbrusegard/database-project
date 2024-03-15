import sqlite3

connection = sqlite3.connect('trondelag_theatre.db')

cursor = connection.cursor()

cursor.execute('SELECT id FROM plays WHERE name = ?', ("Størst av alt er kjærligheten"))
play_id = cursor.fetchone()[0]

cursor.execute('SELECT id FROM showings WHERE play_id = ? AND time = ?', (play_id, "2024-02-03 19:00:00"))
showing_id = cursor.fetchone()[0]

cursor.execute("SELECT id, price FROM ticket_prices WHERE group_category = ? AND play_id = ?", ("Ordinary", play_id))
ticket_price_id, ticket_price = cursor.fetchone()