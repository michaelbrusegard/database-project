import sqlite3

connection = sqlite3.connect('trondelag_theatre.db')

cursor = connection.cursor()

with open('schema.sql', 'r') as f:
    schema = f.read()

cursor.executescript(schema)

# Add "Hovedscenen" and "Gamle scene" to the halls table
cursor.execute('INSERT INTO halls (name) VALUES ("Hovedscenen")')
hovedscenen_hall_id = cursor.lastrowid
cursor.execute('INSERT INTO halls (name) VALUES ("Gamle scene")')
gamle_scene_hall_id = cursor.lastrowid

# Add the plays "Kongsemnene" and "Størst av alt er kjærligheten" to the plays table
cursor.execute('INSERT INTO plays (name, hall_id) VALUES ("Kongsemnene", ?)', (hovedscenen_hall_id,))
kongsemnene_play_id = cursor.lastrowid
cursor.execute('INSERT INTO plays (name, hall_id) VALUES ("Størst av alt er kjærligheten", ?)', (gamle_scene_hall_id,))
storst_av_alt_er_kjaerligheten_play_id = cursor.lastrowid


# Add showings for the plays "Kongsemnene" and "Størst av alt er kjærligheten" to the showings table with the times specified in the assignment

# 1. feb, 2. feb, 3, feb, 5. feb og 6. feb at 19:00 for "Kongsemnene"
cursor.execute('INSERT INTO showings (time, play_id) VALUES (?, ?)', ("2024-02-01 19:00:00", kongsemnene_play_id))
cursor.execute('INSERT INTO showings (time, play_id) VALUES (?, ?)', ("2024-02-02 19:00:00", kongsemnene_play_id))
cursor.execute('INSERT INTO showings (time, play_id) VALUES (?, ?)', ("2024-02-03 19:00:00", kongsemnene_play_id))
kongsemnene_3feb_showing_id = cursor.lastrowid
cursor.execute('INSERT INTO showings (time, play_id) VALUES (?, ?)', ("2024-02-05 19:00:00", kongsemnene_play_id))
cursor.execute('INSERT INTO showings (time, play_id) VALUES (?, ?)', ("2024-02-06 19:00:00", kongsemnene_play_id))

# 3. feb, 6. feb, 7. feb, 12. feb, 13. feb og 14. feb at 18:30 for "Størst av alt er kjærligheten"
cursor.execute('INSERT INTO showings (time, play_id) VALUES (?, ?)', ("2024-03-01 18:30:00", storst_av_alt_er_kjaerligheten_play_id))
cursor.execute('INSERT INTO showings (time, play_id) VALUES (?, ?)', ("2024-06-02 18:30:00", storst_av_alt_er_kjaerligheten_play_id))
cursor.execute('INSERT INTO showings (time, play_id) VALUES (?, ?)', ("2024-07-03 18:30:00", storst_av_alt_er_kjaerligheten_play_id))
cursor.execute('INSERT INTO showings (time, play_id) VALUES (?, ?)', ("2024-12-05 18:30:00", storst_av_alt_er_kjaerligheten_play_id))
cursor.execute('INSERT INTO showings (time, play_id) VALUES (?, ?)', ("2024-13-01 18:30:00", storst_av_alt_er_kjaerligheten_play_id))
cursor.execute('INSERT INTO showings (time, play_id) VALUES (?, ?)', ("2024-14-02 18:30:00", storst_av_alt_er_kjaerligheten_play_id))

# Add the ticket prices for "Kongsemnene" from the assignment
cursor.execute('INSERT INTO ticket_prices (group, price, play_id) VALUES (?, ?, ?)', ("Ordinary", 450, kongsemnene_play_id))
cursor.execute('INSERT INTO ticket_prices (group, price, play_id) VALUES (?, ?, ?)', ("Honour", 380, kongsemnene_play_id))
cursor.execute('INSERT INTO ticket_prices (group, price, play_id) VALUES (?, ?, ?)', ("Student", 280, kongsemnene_play_id))
cursor.execute('INSERT INTO ticket_prices (group, price, play_id) VALUES (?, ?, ?)', ("Group 10", 420, kongsemnene_play_id))
group10_kongsemnene_ticket_price_id = cursor.lastrowid
cursor.execute('INSERT INTO ticket_prices (group, price, play_id) VALUES (?, ?, ?)', ("Group honours 10", 360, kongsemnene_play_id))

# Add the ticket prices for "Størst av alt er kjærligheten" from the assignment
cursor.execute('INSERT INTO ticket_prices (group, price, play_id) VALUES (?, ?, ?)', ("Ordinary", 350, storst_av_alt_er_kjaerligheten_play_id))
cursor.execute('INSERT INTO ticket_prices (group, price, play_id) VALUES (?, ?, ?)', ("Honour", 300, storst_av_alt_er_kjaerligheten_play_id))
cursor.execute('INSERT INTO ticket_prices (group, price, play_id) VALUES (?, ?, ?)', ("Student", 220, storst_av_alt_er_kjaerligheten_play_id))
cursor.execute('INSERT INTO ticket_prices (group, price, play_id) VALUES (?, ?, ?)', ("Children", 220, storst_av_alt_er_kjaerligheten_play_id))
cursor.execute('INSERT INTO ticket_prices (group, price, play_id) VALUES (?, ?, ?)', ("Group 10", 320, storst_av_alt_er_kjaerligheten_play_id))
cursor.execute('INSERT INTO ticket_prices (group, price, play_id) VALUES (?, ?, ?)', ("Group honours 10", 270, storst_av_alt_er_kjaerligheten_play_id))

# Create a standard "customer" called "Trondheim teater", with address "tk.postmottak@trondheim.kommune.no" and mobile number "95198673"
cursor.execute('INSERT INTO customers (name, mobile_number, mobile) VALUES (?, ?, ?)', ("Trondheim teater", "95198673", "tk.postmottak@trondheim.kommune.no"))
trondheim_teater_customer_id = cursor.lastrowid

# Create a big ticket purchase for the "Kongsemnene" play on the 1st of January at 00:00 for the "Trondheim teater" customer
cursor.execute('INSERT INTO ticket_purchases (time, customer_id) VALUES (?, ?)', ("2024-01-01 00:00:00", trondheim_teater_customer_id))
kongsemnene_ticket_purchase_id = cursor.lastrowid

# Create a big ticket purchase for the "Størst av alt er kjærligheten" play on the 1st of January at 00:00 for the "Trondheim teater" customer
cursor.execute('INSERT INTO ticket_purchases (time, customer_id) VALUES (?, ?)', ("2024-01-01 00:00:00", trondheim_teater_customer_id))
storst_av_alt_er_kjaerligheten_ticket_purchase_id = cursor.lastrowid

# Add seats and areas to the "Hovedscenen" hall
with open('hovedscenen.txt', 'r') as f:
    lines = f.readlines()

# Initialize variables
current_area = None
seat_number = 0

# Iterate over each line in the file
for i, line in enumerate(lines):
    # Skip the first line
    if i == 0:
        continue

    line = line.strip()  # Remove trailing newline

    # Check if the line contains a word or a series of characters
    if line.isalpha():
        # Add an area
        cursor.execute('INSERT INTO areas (name, hall_id) VALUES (?, ?)', (line, hovedscenen_hall_id))
        current_area = cursor.lastrowid
    else:
        # Iterate over each character and create a seat only if the character is '0' or '1'
        for j, char in enumerate(line):
            if char == '0':
                seat_number += 1
                cursor.execute('INSERT INTO seats (row_number, chair_number, area_id) VALUES (?, ?, ?)', (i, seat_number, current_area))
            elif char == '1':
                seat_number += 1
                cursor.execute('INSERT INTO seats (row_number, chair_number, area_id) VALUES (?, ?, ?)', (i, seat_number, current_area))
                seat_id = cursor.lastrowid
                cursor.execute('INSERT INTO tickets (showing_id, seat_id, ticket_purchase_id, ticket_price_id) VALUES (?, ?, ?, ?)', (kongsemnene_3feb_showing_id, seat_id, kongsemnene_ticket_purchase_id, group10_kongsemnene_ticket_price_id))
                



connection.commit()
connection.close()