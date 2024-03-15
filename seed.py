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
cursor.execute('INSERT INTO showings (time, play_id) VALUES (?, ?)', ("2024-02-03 18:30:00", storst_av_alt_er_kjaerligheten_play_id))
storst_av_alt_er_kjaerligheten_3feb_showing_id = cursor.lastrowid
cursor.execute('INSERT INTO showings (time, play_id) VALUES (?, ?)', ("2024-02-06 18:30:00", storst_av_alt_er_kjaerligheten_play_id))
cursor.execute('INSERT INTO showings (time, play_id) VALUES (?, ?)', ("2024-02-07 18:30:00", storst_av_alt_er_kjaerligheten_play_id))
cursor.execute('INSERT INTO showings (time, play_id) VALUES (?, ?)', ("2024-02-12 18:30:00", storst_av_alt_er_kjaerligheten_play_id))
cursor.execute('INSERT INTO showings (time, play_id) VALUES (?, ?)', ("2024-02-13 18:30:00", storst_av_alt_er_kjaerligheten_play_id))
cursor.execute('INSERT INTO showings (time, play_id) VALUES (?, ?)', ("2024-02-14 18:30:00", storst_av_alt_er_kjaerligheten_play_id))

# Add the ticket prices for "Kongsemnene" from the assignment
cursor.execute('INSERT INTO ticket_prices (group_category, price, play_id) VALUES (?, ?, ?)', ("Ordinary", 450, kongsemnene_play_id))
cursor.execute('INSERT INTO ticket_prices (group_category, price, play_id) VALUES (?, ?, ?)', ("Honour", 380, kongsemnene_play_id))
cursor.execute('INSERT INTO ticket_prices (group_category, price, play_id) VALUES (?, ?, ?)', ("Student", 280, kongsemnene_play_id))
cursor.execute('INSERT INTO ticket_prices (group_category, price, play_id) VALUES (?, ?, ?)', ("Group 10", 420, kongsemnene_play_id))
group_10_kongsemnene_ticket_price_id = cursor.lastrowid
cursor.execute('INSERT INTO ticket_prices (group_category, price, play_id) VALUES (?, ?, ?)', ("Group honours 10", 360, kongsemnene_play_id))

# Add the ticket prices for "Størst av alt er kjærligheten" from the assignment
cursor.execute('INSERT INTO ticket_prices (group_category, price, play_id) VALUES (?, ?, ?)', ("Ordinary", 350, storst_av_alt_er_kjaerligheten_play_id))
cursor.execute('INSERT INTO ticket_prices (group_category, price, play_id) VALUES (?, ?, ?)', ("Honour", 300, storst_av_alt_er_kjaerligheten_play_id))
cursor.execute('INSERT INTO ticket_prices (group_category, price, play_id) VALUES (?, ?, ?)', ("Student", 220, storst_av_alt_er_kjaerligheten_play_id))
cursor.execute('INSERT INTO ticket_prices (group_category, price, play_id) VALUES (?, ?, ?)', ("Children", 220, storst_av_alt_er_kjaerligheten_play_id))
cursor.execute('INSERT INTO ticket_prices (group_category, price, play_id) VALUES (?, ?, ?)', ("Group 10", 320, storst_av_alt_er_kjaerligheten_play_id))
group_10_storst_av_alt_er_kjaerligheten_ticket_price_id = cursor.lastrowid
cursor.execute('INSERT INTO ticket_prices (group_category, price, play_id) VALUES (?, ?, ?)', ("Group honours 10", 270, storst_av_alt_er_kjaerligheten_play_id))

# Create a standard "customer" called "Trondheim teater", with address "tk.postmottak@trondheim.kommune.no" and mobile number "95198673"
cursor.execute('INSERT INTO customers (name, mobile_number, address) VALUES (?, ?, ?)', ("Trondheim teater", "95198673", "tk.postmottak@trondheim.kommune.no"))
trondheim_teater_customer_id = cursor.lastrowid

# Create a big ticket purchase for the "Kongsemnene" play on the 1st of January at 00:00 for the "Trondheim teater" customer
cursor.execute('INSERT INTO ticket_purchases (time, customer_id) VALUES (?, ?)', ("2024-01-01 00:00:00", trondheim_teater_customer_id))
kongsemnene_ticket_purchase_id = cursor.lastrowid

# Create a big ticket purchase for the "Størst av alt er kjærligheten" play on the 1st of January at 00:00 for the "Trondheim teater" customer
cursor.execute('INSERT INTO ticket_purchases (time, customer_id) VALUES (?, ?)', ("2024-01-01 00:00:00", trondheim_teater_customer_id))
storst_av_alt_er_kjaerligheten_ticket_purchase_id = cursor.lastrowid

# Add seats and areas to the "Hovedscenen" hall
with open('files needed/hovedscenen.txt', 'r') as f:
    lines = f.readlines()

hovedscenen_areas = []

for i, line in enumerate(lines):
    if i == 0:
        continue

    line = line.strip() 

    if line.isalpha():
        cursor.execute('INSERT INTO areas (name, hall_id) VALUES (?, ?)', (line, hovedscenen_hall_id))
        hovedscenen_areas.append(cursor.lastrowid)

# Initialize variables
current_area = hovedscenen_areas.pop()
seat_number = 0
row_number = 0

# Iterate over each line in the file
for i, line in reversed(list(enumerate(lines))):
    # Skip the first line and the second line
    if i == 0 or i == 1:
        continue

    line = line.strip()  # Remove trailing newline
    # Check if the line contains a word or a series of characters
    if line.isalpha():
        current_area = hovedscenen_areas.pop()
    else:
        row_number += 1
        # Iterate over each character and create a seat only if the character is '0' or '1'
        for j, char in enumerate(line):
            seat_number += 1
            if char == '0':
                cursor.execute('INSERT INTO seats (row_number, chair_number, hall_id, area_id) VALUES (?, ?, ?, ?)', (row_number, seat_number, hovedscenen_hall_id, current_area))
                
            elif char == '1':
                cursor.execute('INSERT INTO seats (row_number, chair_number, hall_id, area_id) VALUES (?, ?, ?, ?)', (row_number, seat_number, hovedscenen_hall_id, current_area))
                seat_id = cursor.lastrowid
                cursor.execute('INSERT INTO tickets (showing_id, seat_id, ticket_purchase_id, ticket_price_id) VALUES (?, ?, ?, ?)', (kongsemnene_3feb_showing_id, seat_id, kongsemnene_ticket_purchase_id, group_10_kongsemnene_ticket_price_id))

with open('files needed/gamle-scene.txt', 'r') as f:
    lines = f.readlines()

current_area_name = None
areas_row_count = {}  # Dictionary to keep track of rows for each area
current_area = None

# First Pass: Count rows for each area
for i, line in enumerate(lines):
    if i == 0:  # Skip the first line
        continue

    line = line.strip()

    if not line.isdigit():  # New area
        current_area_name = line
        areas_row_count[current_area_name] = 0
    else:
        areas_row_count[current_area_name] += 1

# Reset for Second Pass
current_area_name = None

# Second Pass: Insert seats with reversed row numbers
for i, line in enumerate(lines):
    if i == 0:  # Skip the first line
        continue

    line = line.strip()

    if not line.isdigit():  # New area
        current_area_name = line
        # Insert area and get its ID
        cursor.execute('INSERT INTO areas (name, hall_id) VALUES (?, ?)', (line, gamle_scene_hall_id))
        current_area = cursor.lastrowid
    else:
        # Calculate the reversed row number
        current_row_number = areas_row_count[current_area_name]
        areas_row_count[current_area_name] -= 1  # Decrement for next row
        seat_number = 0

        for char in line:
            seat_number += 1
            if char in ['0', '1']:
                # Insert seat
                cursor.execute('INSERT INTO seats (row_number, chair_number, hall_id, area_id) VALUES (?, ?, ?, ?)', 
                               (current_row_number, seat_number, gamle_scene_hall_id, current_area))
                if char == '1':  # Seat is taken, insert a ticket
                    seat_id = cursor.lastrowid
                    cursor.execute('INSERT INTO tickets (showing_id, seat_id, ticket_purchase_id, ticket_price_id) VALUES (?, ?, ?, ?)', 
                                   (storst_av_alt_er_kjaerligheten_3feb_showing_id, seat_id, storst_av_alt_er_kjaerligheten_ticket_purchase_id, group_10_storst_av_alt_er_kjaerligheten_ticket_price_id))

# Add the acts for the "Kongsemnene" play
cursor.execute('INSERT INTO acts (number, name, play_id) VALUES (?, ?, ?)', (1, "Act 1", kongsemnene_play_id))
kongsemnene_act1_id = cursor.lastrowid
cursor.execute('INSERT INTO acts (number, name, play_id) VALUES (?, ?, ?)', (2, "Act 2", kongsemnene_play_id))
kongsemnene_act2_id = cursor.lastrowid
cursor.execute('INSERT INTO acts (number, name, play_id) VALUES (?, ?, ?)', (3, "Act 3", kongsemnene_play_id))
kongsemnene_act3_id = cursor.lastrowid
cursor.execute('INSERT INTO acts (number, name, play_id) VALUES (?, ?, ?)', (4, "Act 4", kongsemnene_play_id))
kongsemnene_act4_id = cursor.lastrowid
cursor.execute('INSERT INTO acts (number, name, play_id) VALUES (?, ?, ?)', (5, "Act 5", kongsemnene_play_id))
kongsemnene_act5_id = cursor.lastrowid

# Add the acts for the "Størst av alt er kjærligheten" play
cursor.execute('INSERT INTO acts (number, name, play_id) VALUES (?, ?, ?)', (1, "Act 1", storst_av_alt_er_kjaerligheten_play_id))
storst_av_alt_er_kjaerligheten_act1_id = cursor.lastrowid

# Add the roles for the "Kongsemnene" play
cursor.execute('INSERT INTO roles (name) VALUES (?)', ("Håkon Håkonson",))
hakon_hakonson_role_id = cursor.lastrowid
cursor.execute('INSERT INTO roles (name) VALUES (?)', ("Dagfinn Bonde",))
dagfinn_bonde_role_id = cursor.lastrowid
cursor.execute('INSERT INTO roles (name) VALUES (?)', ("Sigrid",))
sigrid_role_id = cursor.lastrowid
cursor.execute('INSERT INTO roles (name) VALUES (?)', ("Jatgeir Skald",))
jatgeir_skald_role_id = cursor.lastrowid
cursor.execute('INSERT INTO roles (name) VALUES (?)', ("Ingebjørg",))
ingebjørg_role_id = cursor.lastrowid
cursor.execute('INSERT INTO roles (name) VALUES (?)', ("Guttorm Ingesson",))
guttorm_ingesson_role_id = cursor.lastrowid
cursor.execute('INSERT INTO roles (name) VALUES (?)', ("Skule Jarl",))
skule_jarl_role_id = cursor.lastrowid
cursor.execute('INSERT INTO roles (name) VALUES (?)', ("Inga frå Varteig",))
inga_fra_varteig_role_id = cursor.lastrowid
cursor.execute('INSERT INTO roles (name) VALUES (?)', ("Paal Flida",))
paal_flida_role_id = cursor.lastrowid
cursor.execute('INSERT INTO roles (name) VALUES (?)', ("Ragnhild",))
ragnhild_role_id = cursor.lastrowid
cursor.execute('INSERT INTO roles (name) VALUES (?)', ("Gregorius Jonsson",))
gregorius_jonsson_role_id = cursor.lastrowid
cursor.execute('INSERT INTO roles (name) VALUES (?)', ("Margrete",))
margrete_role_id = cursor.lastrowid
cursor.execute('INSERT INTO roles (name) VALUES (?)', ("Biskop Nikolas",))
biskop_nikolas_role_id = cursor.lastrowid
cursor.execute('INSERT INTO roles (name) VALUES (?)', ("Peter",))
peter_role_id = cursor.lastrowid
cursor.execute('INSERT INTO roles (name) VALUES (?)', ("Trønder",))
tronder_role_id = cursor.lastrowid
cursor.execute('INSERT INTO roles (name) VALUES (?)', ("Baard Bratte",))
baard_bratte_role_id = cursor.lastrowid

# Add roles to the "Størst av alt er kjærligheten" play
cursor.execute('INSERT INTO roles (name) VALUES (?)', ("Sunniva Du Mond Nordal",))
sunniva_du_mond_nordal_role_id = cursor.lastrowid
cursor.execute('INSERT INTO roles (name) VALUES (?)', ("Jo Saberniak",))
jo_saberniak_role_id = cursor.lastrowid
cursor.execute('INSERT INTO roles (name) VALUES (?)', ("Marte M Steinholt",))
marte_m_steinholt_role_id = cursor.lastrowid
cursor.execute('INSERT INTO roles (name) VALUES (?)', ("Tor Ivar Hagen",))
tor_ivar_hagen_role_id = cursor.lastrowid
cursor.execute('INSERT INTO roles (name) VALUES (?)', ("Trond-Ove Skrødal",))
trond_ove_skrodal_role_id = cursor.lastrowid
cursor.execute('INSERT INTO roles (name) VALUES (?)', ("Natalie Grøndahl Tangen",))
natalie_grondahl_tangen_role_id = cursor.lastrowid
cursor.execute('INSERT INTO roles (name) VALUES (?)', ("Åsmund Flaten",))
asmund_flaten_role_id = cursor.lastrowid

# Add actors to the "Størst av alt er kjærligheten" play
cursor.execute('INSERT INTO actors (name) VALUES (?)', ("Sunniva Du Mond Nordal",))
sunniva_du_mond_nordal_actor_id = cursor.lastrowid
cursor.execute('INSERT INTO actors (name) VALUES (?)', ("Jo Saberniak",))
jo_saberniak_actor_id = cursor.lastrowid
cursor.execute('INSERT INTO actors (name) VALUES (?)', ("Marte M Steinholt",))
marte_m_steinholt_actor_id = cursor.lastrowid
cursor.execute('INSERT INTO actors (name) VALUES (?)', ("Tor Ivar Hagen",))
tor_ivar_hagen_actor_id = cursor.lastrowid
cursor.execute('INSERT INTO actors (name) VALUES (?)', ("Trond-Ove Skrødal",))
trond_ove_skrodal_actor_id = cursor.lastrowid
cursor.execute('INSERT INTO actors (name) VALUES (?)', ("Natalie Grøndahl Tangen",))
natalie_grondahl_tangen_actor_id = cursor.lastrowid
cursor.execute('INSERT INTO actors (name) VALUES (?)', ("Åsmund Flaten",))
asmund_flaten_actor_id = cursor.lastrowid

# Add actors to the "Kongsemnene" play
cursor.execute('INSERT INTO actors (name) VALUES (?)', ("Arturo Scotti",))
arturo_scotti_actor_id = cursor.lastrowid
cursor.execute('INSERT INTO actors (name) VALUES (?)', ("Ingunn Beate Strige Øyen",))
ingunn_beate_strige_oyen_actor_id = cursor.lastrowid
cursor.execute('INSERT INTO actors (name) VALUES (?)', ("Hans Petter Nilsen",))
hans_petter_nilsen_actor_id = cursor.lastrowid
cursor.execute('INSERT INTO actors (name) VALUES (?)', ("Synnøve Fossum Eriksen",))
synnove_fossum_eriksen_actor_id = cursor.lastrowid
cursor.execute('INSERT INTO actors (name) VALUES (?)', ("Emma Caroline Deichmann",))
emma_caroline_deichmann_actor_id = cursor.lastrowid
cursor.execute('INSERT INTO actors (name) VALUES (?)', ("Thomas Jensen Takyi",))
thomas_jensen_takyi_actor_id = cursor.lastrowid
cursor.execute('INSERT INTO actors (name) VALUES (?)', ("Per Bogstad Gulliksen",))
per_bogstad_gulliksen_actor_id = cursor.lastrowid
cursor.execute('INSERT INTO actors (name) VALUES (?)', ("Isak Holkem Sørensen",))
isak_holkem_sorensen_actor_id = cursor.lastrowid
cursor.execute('INSERT INTO actors (name) VALUES (?)', ("Fabian Heidelberg Lunde",))
fabian_heidelberg_lunde_actor_id = cursor.lastrowid
cursor.execute('INSERT INTO actors (name) VALUES (?)', ("Emil Olafsson",))
emil_olafsson_actor_id = cursor.lastrowid
cursor.execute('INSERT INTO actors (name) VALUES (?)', ("Snorre Ryen Tøndel",))
snorre_ryen_tondel_actor_id = cursor.lastrowid
cursor.execute('INSERT INTO actors (name) VALUES (?)', ("Madeleine Brantzæg Nilsen",))
madeleine_brantzaeg_nilsen_actor_id = cursor.lastrowid

# Add the played_by relationships for the "Størst av alt er kjærligheten" play
cursor.execute('INSERT INTO played_by (role_id, actor_id) VALUES (?, ?)', (sunniva_du_mond_nordal_role_id, sunniva_du_mond_nordal_actor_id))
cursor.execute('INSERT INTO played_by (role_id, actor_id) VALUES (?, ?)', (jo_saberniak_role_id, jo_saberniak_actor_id))
cursor.execute('INSERT INTO played_by (role_id, actor_id) VALUES (?, ?)', (marte_m_steinholt_role_id, marte_m_steinholt_actor_id))
cursor.execute('INSERT INTO played_by (role_id, actor_id) VALUES (?, ?)', (tor_ivar_hagen_role_id, tor_ivar_hagen_actor_id))
cursor.execute('INSERT INTO played_by (role_id, actor_id) VALUES (?, ?)', (trond_ove_skrodal_role_id, trond_ove_skrodal_actor_id))
cursor.execute('INSERT INTO played_by (role_id, actor_id) VALUES (?, ?)', (natalie_grondahl_tangen_role_id, natalie_grondahl_tangen_actor_id))
cursor.execute('INSERT INTO played_by (role_id, actor_id) VALUES (?, ?)', (asmund_flaten_role_id, asmund_flaten_actor_id))

# Add the roles_in_act relationships for the "Størst av alt er kjærligheten" play
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (storst_av_alt_er_kjaerligheten_act1_id, sunniva_du_mond_nordal_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (storst_av_alt_er_kjaerligheten_act1_id, jo_saberniak_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (storst_av_alt_er_kjaerligheten_act1_id, marte_m_steinholt_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (storst_av_alt_er_kjaerligheten_act1_id, tor_ivar_hagen_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (storst_av_alt_er_kjaerligheten_act1_id, trond_ove_skrodal_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (storst_av_alt_er_kjaerligheten_act1_id, natalie_grondahl_tangen_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (storst_av_alt_er_kjaerligheten_act1_id, asmund_flaten_role_id))

# Add the played_by relationships for the "Kongsemnene" play
cursor.execute('INSERT INTO played_by (role_id, actor_id) VALUES (?, ?)', (hakon_hakonson_role_id, arturo_scotti_actor_id))
cursor.execute('INSERT INTO played_by (role_id, actor_id) VALUES (?, ?)', (inga_fra_varteig_role_id, ingunn_beate_strige_oyen_actor_id))
cursor.execute('INSERT INTO played_by (role_id, actor_id) VALUES (?, ?)', (skule_jarl_role_id, hans_petter_nilsen_actor_id))
cursor.execute('INSERT INTO played_by (role_id, actor_id) VALUES (?, ?)', (ragnhild_role_id, madeleine_brantzaeg_nilsen_actor_id))
cursor.execute('INSERT INTO played_by (role_id, actor_id) VALUES (?, ?)', (margrete_role_id, synnove_fossum_eriksen_actor_id))
cursor.execute('INSERT INTO played_by (role_id, actor_id) VALUES (?, ?)', (sigrid_role_id, emma_caroline_deichmann_actor_id))
cursor.execute('INSERT INTO played_by (role_id, actor_id) VALUES (?, ?)', (ingebjørg_role_id, emma_caroline_deichmann_actor_id))
cursor.execute('INSERT INTO played_by (role_id, actor_id) VALUES (?, ?)', (biskop_nikolas_role_id, thomas_jensen_takyi_actor_id))
cursor.execute('INSERT INTO played_by (role_id, actor_id) VALUES (?, ?)', (gregorius_jonsson_role_id, per_bogstad_gulliksen_actor_id))
cursor.execute('INSERT INTO played_by (role_id, actor_id) VALUES (?, ?)', (paal_flida_role_id, isak_holkem_sorensen_actor_id))
cursor.execute('INSERT INTO played_by (role_id, actor_id) VALUES (?, ?)', (tronder_role_id, isak_holkem_sorensen_actor_id))
cursor.execute('INSERT INTO played_by (role_id, actor_id) VALUES (?, ?)', (baard_bratte_role_id, fabian_heidelberg_lunde_actor_id))
cursor.execute('INSERT INTO played_by (role_id, actor_id) VALUES (?, ?)', (tronder_role_id, fabian_heidelberg_lunde_actor_id))
cursor.execute('INSERT INTO played_by (role_id, actor_id) VALUES (?, ?)', (jatgeir_skald_role_id, emil_olafsson_actor_id))
cursor.execute('INSERT INTO played_by (role_id, actor_id) VALUES (?, ?)', (dagfinn_bonde_role_id, emil_olafsson_actor_id))
cursor.execute('INSERT INTO played_by (role_id, actor_id) VALUES (?, ?)', (peter_role_id, snorre_ryen_tondel_actor_id))


# Add the roles_in_act relationships for the "Kongsemnene" play
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act1_id, hakon_hakonson_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act2_id, hakon_hakonson_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act3_id, hakon_hakonson_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act4_id, hakon_hakonson_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act5_id, hakon_hakonson_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act1_id, dagfinn_bonde_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act2_id, dagfinn_bonde_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act3_id, dagfinn_bonde_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act4_id, dagfinn_bonde_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act5_id, dagfinn_bonde_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act4_id, jatgeir_skald_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act1_id, sigrid_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act2_id, sigrid_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act5_id, sigrid_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act4_id, ingebjørg_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act1_id, guttorm_ingesson_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act1_id, skule_jarl_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act2_id, skule_jarl_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act3_id, skule_jarl_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act4_id, skule_jarl_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act5_id, skule_jarl_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act1_id, inga_fra_varteig_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act3_id, inga_fra_varteig_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act1_id, paal_flida_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act2_id, paal_flida_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act3_id, paal_flida_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act4_id, paal_flida_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act5_id, paal_flida_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act1_id, ragnhild_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act5_id, ragnhild_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act1_id, gregorius_jonsson_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act2_id, gregorius_jonsson_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act3_id, gregorius_jonsson_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act4_id, gregorius_jonsson_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act5_id, gregorius_jonsson_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act1_id, margrete_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act2_id, margrete_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act3_id, margrete_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act4_id, margrete_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act5_id, margrete_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act1_id, biskop_nikolas_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act2_id, biskop_nikolas_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act3_id, biskop_nikolas_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act3_id, peter_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act4_id, peter_role_id))
cursor.execute('INSERT INTO roles_in_act (act_id, role_id) VALUES (?, ?)', (kongsemnene_act5_id, peter_role_id))

# Add employees to the employees table
cursor.execute('INSERT INTO employees (name, email, status) VALUES (?, ?, ?)', ("Jonas Corell Petersen", "korall@mail.com", "Fast ansatt"))
jonas_corell_petersen_employee_id = cursor.lastrowid
cursor.execute('INSERT INTO employees (name, email, status) VALUES (?, ?, ?)', ("Magnus Mikaelsen", "magnusdenstore@mail.com", "Fast ansatt"))
magnus_mikaelsen_employee_id = cursor.lastrowid
cursor.execute('INSERT INTO employees (name, email, status) VALUES (?, ?, ?)', ("David Gehrt", "gris@gmail.com", "Fast ansatt"))
david_gehrt_employee_id = cursor.lastrowid
cursor.execute('INSERT INTO employees (name, email, status) VALUES (?, ?, ?)', ("Kristoffer Spender", "bigspender@mail.com", "Fast ansatt"))
kristoffer_spender_employee_id = cursor.lastrowid
cursor.execute('INSERT INTO employees (name, email, status) VALUES (?, ?, ?)', ("Gaute Tønder", "tønderstruck@mail.com", "Fast ansatt"))
gaute_tonder_employee_id = cursor.lastrowid
cursor.execute('INSERT INTO employees (name, email, status) VALUES (?, ?, ?)', ("Yury Butusov", "yogibear@mail.com", "Fast ansatt"))
yury_butusov_employee_id = cursor.lastrowid
cursor.execute('INSERT INTO employees (name, email, status) VALUES (?, ?, ?)', ("Mina Rype Stokke", "rypapåstokken@twitter.no", "Fast ansatt"))
mina_rype_stokke_employee_id = cursor.lastrowid
cursor.execute('INSERT INTO employees (name, email, status) VALUES (?, ?, ?)', ("Aleksandr Shinshkin-Hokusai", "nametoolong@mail.com", "Innleid"))
aleksandr_shinshkin_hokusai_employee_id = cursor.lastrowid
cursor.execute('INSERT INTO employees (name, email, status) VALUES (?, ?, ?)', ("Eivind Myren", "myrra@mvismann.no", "Frivillig"))
eivind_myren_employee_id = cursor.lastrowid

# Add tasks to the "Kongsemnene" play
cursor.execute('INSERT INTO tasks (description, play_id, employee_id) VALUES (?, ?, ?)', ("Regi", kongsemnene_play_id, yury_butusov_employee_id))
cursor.execute('INSERT INTO tasks (description, play_id, employee_id) VALUES (?, ?, ?)', ("Musikkutvelgelse", kongsemnene_play_id, yury_butusov_employee_id))
cursor.execute('INSERT INTO tasks (description, play_id, employee_id) VALUES (?, ?, ?)', ("Scenografi og kostymer", kongsemnene_play_id, aleksandr_shinshkin_hokusai_employee_id))
cursor.execute('INSERT INTO tasks (description, play_id, employee_id) VALUES (?, ?, ?)', ("Lysdesign", kongsemnene_play_id, eivind_myren_employee_id))
cursor.execute('INSERT INTO tasks (description, play_id, employee_id) VALUES (?, ?, ?)', ("Dramaturg", kongsemnene_play_id, mina_rype_stokke_employee_id))

# Add tasks to the "Størst av alt er kjærligheten" play
cursor.execute('INSERT INTO tasks (description, play_id, employee_id) VALUES (?, ?, ?)', ("Regi", storst_av_alt_er_kjaerligheten_play_id, jonas_corell_petersen_employee_id))
cursor.execute('INSERT INTO tasks (description, play_id, employee_id) VALUES (?, ?, ?)', ("Musikalsk ansvarlig", storst_av_alt_er_kjaerligheten_play_id, gaute_tonder_employee_id))
cursor.execute('INSERT INTO tasks (description, play_id, employee_id) VALUES (?, ?, ?)', ("Scenografi og kostymer", storst_av_alt_er_kjaerligheten_play_id, david_gehrt_employee_id))
cursor.execute('INSERT INTO tasks (description, play_id, employee_id) VALUES (?, ?, ?)', ("Lysdesign", storst_av_alt_er_kjaerligheten_play_id, magnus_mikaelsen_employee_id)) 
cursor.execute('INSERT INTO tasks (description, play_id, employee_id) VALUES (?, ?, ?)', ("Dramaturg", storst_av_alt_er_kjaerligheten_play_id, kristoffer_spender_employee_id))

connection.commit()
connection.close()
