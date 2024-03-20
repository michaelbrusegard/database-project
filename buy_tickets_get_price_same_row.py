import sqlite3
from datetime import datetime

connection = sqlite3.connect('trondelag_theatre.db')
cursor = connection.cursor()

def create_customer(name, mobile_number, address):
    try:
        cursor.execute("""
            SELECT id FROM customers WHERE name = ? AND mobile_number = ? AND address = ?
        """, (name, mobile_number, address))
        customer = cursor.fetchone()
        if customer is not None:
            return customer[0]

        cursor.execute("""
            INSERT INTO customers (name, mobile_number, address)
            VALUES (?, ?, ?)
        """, (name, mobile_number, address))
        connection.commit()
        return cursor.lastrowid
    except Exception as e:
        print(f"Error occurred while creating or fetching customer: {e}")
def create_ticket_purchase(customer_id):
    try:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("""
            INSERT INTO ticket_purchases (time, customer_id)
            VALUES (?, ?)
        """, (current_time, customer_id))
        connection.commit()
        return cursor.lastrowid
    except Exception as e:
        print(f"Error occurred while creating ticket purchase: {e}")

def buy_tickets_get_price_same_row(play_name, date, group_category, amount, name, mobile_number, address):
    cursor.execute('SELECT id, name, hall_id FROM plays WHERE name = ?', (play_name,))
    play_id, play_name, hall_id = cursor.fetchone()

    if play_id is None:
        print(f"The play {play_name} does not exist.")
        return

    if hall_id is None:
        print(f"The play {play_name} does not have a hall assigned to it.")
        return

    cursor.execute('SELECT id FROM showings WHERE play_id = ? AND substr(time, 1, 10) = ?', (play_id, date))
    showing_id = cursor.fetchone()[0]

    if showing_id is None:
        print(f"The play {play_name} does not have a showing on {date}.")
        return

    cursor.execute('SELECT name FROM halls WHERE id = ?', (hall_id,))
    hall_name = cursor.fetchone()[0]

    if hall_name is None:
        print(f"The hall for the play {play_name} does not exist.")
        return

    cursor.execute("SELECT id, price FROM ticket_prices WHERE group_category = ? AND play_id = ?", (group_category, play_id))
    ticket_price_id, ticket_price = cursor.fetchone()

    if ticket_price_id is None:
        print(f"The ticket price for the play {play_name} and group category {group_category} does not exist.")
        return

    cursor.execute("""
        SELECT seats.row_number, areas.name
        FROM seats 
        LEFT JOIN tickets ON seats.id = tickets.seat_id AND tickets.showing_id = ?
        LEFT JOIN areas ON seats.area_id = areas.id
        WHERE tickets.seat_id IS NULL AND seats.hall_id = ?
        GROUP BY seats.row_number, seats.area_id
        HAVING COUNT(*) >= ?
        ORDER BY seats.row_number
        LIMIT 1
    """, (showing_id, hall_id, amount))
    row_number, area_name = cursor.fetchone()

    if row_number is None:
        print(f"There are not enough available seats for the play {play_name} on {date}.")
        return

    cursor.execute("""
        SELECT seats.id, seats.chair_number
        FROM seats 
        LEFT JOIN tickets ON seats.id = tickets.seat_id AND tickets.showing_id = ?
        WHERE tickets.seat_id IS NULL AND seats.row_number = ? AND seats.hall_id = ?
        LIMIT ?
    """, (showing_id, row_number, hall_id, amount))
    seat_ids_chair_numbers = cursor.fetchall()
    seat_ids = [row[0] for row in seat_ids_chair_numbers]
    chair_numbers = [row[1] for row in seat_ids_chair_numbers]

    customer_id = create_customer(name, mobile_number, address)
    ticket_purchase_id = create_ticket_purchase(customer_id)

    for seat_id in seat_ids:
        try:
            cursor.execute("""
                INSERT INTO tickets (showing_id, seat_id, ticket_purchase_id, ticket_price_id)
                VALUES (?, ?, ?, ?)
            """, (showing_id, seat_id, ticket_purchase_id, ticket_price_id))
            connection.commit()
        except Exception as e:
            print(f"Error occurred while creating ticket for seat {seat_id}: {e}")

    print(f"You purchased {amount} tickets for {play_name} in the {hall_name} for row number {row_number} with seat numbers {chair_numbers} in {area_name} area for: {ticket_price * amount} kr")

buy_tickets_get_price_same_row('Størst av alt er kjærligheten', '2024-02-03', 'Ordinary', 9, 'Ola Nordmann', '12345678', 'ola@nordmann.no')

connection.close()