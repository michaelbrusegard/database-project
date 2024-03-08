CREATE TABLE halls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE areas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    hall_id INTEGER NOT NULL,
    FOREIGN KEY (hall_id) REFERENCES halls(id)
);

CREATE TABLE seats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chair_number INTEGER NOT NULL,
    row_number INTEGER,
    hall_id INTEGER NOT NULL,
    area_id INTEGER,
    FOREIGN KEY (area_id) REFERENCES areas(id),
    FOREIGN KEY (hall_id) REFERENCES halls(id)
);

CREATE TABLE plays (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    hall_id INTEGER NOT NULL,
    FOREIGN KEY (hall_id) REFERENCES halls(id)
);

CREATE TABLE showings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time TEXT NOT NULL,
    play_id INTEGER NOT NULL,
    FOREIGN KEY (play_id) REFERENCES plays(id)
);

CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    mobile_number TEXT NOT NULL UNIQUE,
    address TEXT NOT NULL
);

CREATE TABLE ticket_purchases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time TEXT NOT NULL,
    customer_id INTEGER NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE TABLE ticket_prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group TEXT NOT NULL,
    price REAL NOT NULL,
    play_id INTEGER NOT NULL,
    FOREIGN KEY (play_id) REFERENCES plays(id)
);

CREATE TABLE tickets (
    showing_id INTEGER NOT NULL,
    seat_id INTEGER NOT NULL,
    ticket_purchase_id INTEGER NOT NULL,
    ticket_price_id INTEGER NOT NULL,
    PRIMARY KEY (showing_id, seat_id, ticket_purchase_id),
    FOREIGN KEY (showing_id) REFERENCES showings(id),
    FOREIGN KEY (seat_id) REFERENCES seats(id),
    FOREIGN KEY (ticket_purchase_id) REFERENCES ticket_purchases(id),
    FOREIGN KEY (ticket_price_id) REFERENCES ticket_prices(id)
);

CREATE TABLE acts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number INTEGER NOT NULL,
    name TEXT,
    play_id INTEGER NOT NULL,
    FOREIGN KEY (play_id) REFERENCES plays(id)
);

CREATE TABLE roles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE roles_in_act (
    act_id INTEGER NOT NULL,
    role_id INTEGER NOT NULL,
    PRIMARY KEY (act_id, role_id),
    FOREIGN KEY (act_id) REFERENCES acts(id),
    FOREIGN KEY (role_id) REFERENCES roles(id)
);

CREATE TABLE actors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE played_by (
    role_id INTEGER NOT NULL,
    actor_id INTEGER NOT NULL,
    PRIMARY KEY (role_id, actor_id),
    FOREIGN KEY (role_id) REFERENCES roles(id),
    FOREIGN KEY (actor_id) REFERENCES actors(id)
);

CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    status TEXT NOT NULL
);

CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    play_id INTEGER NOT NULL,
    employee_id INTEGER NOT NULL,
    FOREIGN KEY (play_id) REFERENCES plays(id),
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);

-- Indexes on foreign keys
CREATE INDEX idx_areas_hall_id ON areas(hall_id);

CREATE INDEX idx_seats_hall_id ON seats(hall_id);

CREATE INDEX idx_seats_area_id ON seats(area_id);

CREATE INDEX idx_plays_hall_id ON plays(hall_id);

CREATE INDEX idx_showings_play_id ON showings(play_id);

CREATE INDEX idx_ticket_purchases_customer_id ON ticket_purchases(customer_id);

CREATE INDEX idx_ticket_prices_play_id ON ticket_prices(play_id);

CREATE INDEX idx_tickets_showing_id ON tickets(showing_id);

CREATE INDEX idx_tickets_seat_id ON tickets(seat_id);

CREATE INDEX idx_tickets_ticket_purchase_id ON tickets(ticket_purchase_id);

CREATE INDEX idx_tickets_ticket_price_id ON tickets(ticket_price_id);

CREATE INDEX idx_acts_play_id ON acts(play_id);

CREATE INDEX idx_roles_in_act_act_id ON roles_in_act(act_id);

CREATE INDEX idx_roles_in_act_role_id ON roles_in_act(role_id);

CREATE INDEX idx_played_by_role_id ON played_by(role_id);

CREATE INDEX idx_played_by_actor_id ON played_by(actor_id);

CREATE INDEX idx_tasks_play_id ON tasks(play_id);

CREATE INDEX idx_tasks_employee_id ON tasks(employee_id);