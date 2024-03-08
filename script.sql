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
    play_id INTEGER NOT NULL,
    time TEXT NOT NULL,
    FOREIGN KEY (play_id) REFERENCES plays(id)
);

CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    mobile_number TEXT NOT NULL,
    address TEXT NOT NULL
);

CREATE TABLE ticket_purchases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    purchase_date TEXT NOT NULL,
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
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    showings_id INTEGER NOT NULL,
    seat_id INTEGER NOT NULL,
    ticket_purchase_id INTEGER NOT NULL,
    ticket_price_id INTEGER NOT NULL,
    FOREIGN KEY (showings_id) REFERENCES showings(id),
    FOREIGN KEY (seat_id) REFERENCES seats(id),
    FOREIGN KEY (ticket_purchase_id) REFERENCES ticket_purchases(id),
    FOREIGN KEY (ticket_price_id) REFERENCES ticket_prices(id)
);

CREATE TABLE actors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE roles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE acts (
    play_id INTEGER NOT NULL,
    number INTEGER NOT NULL,
    name TEXT,
    PRIMARY KEY (play_id, number),
    FOREIGN KEY (play_id) REFERENCES plays(id)
);

CREATE TABLE actor_roles (
    actor_id INTEGER NOT NULL,
    role_id INTEGER NOT NULL,
    act_id INTEGER NOT NULL,
    PRIMARY KEY (actor_id, role_id, act_id),
    FOREIGN KEY (actor_id) REFERENCES actors(id),
    FOREIGN KEY (role_id) REFERENCES roles(id),
    FOREIGN KEY (act_id) REFERENCES acts(id)
);

CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    employee_status TEXT NOT NULL
);

CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    play_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    employee_id INTEGER NOT NULL,
    FOREIGN KEY (play_id) REFERENCES plays(id),
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);

CREATE INDEX idx_hall_id ON areas(hall_id);

CREATE INDEX idx_area_id ON seats(area_id);

CREATE INDEX idx_hall_id_play_id ON plays(hall_id);

CREATE INDEX idx_showings_play_id ON showings(play_id);

CREATE INDEX idx_ticket_purchases_customer_id ON ticket_purchases(customer_id);

CREATE INDEX idx_tickets_showings_id ON tickets(showings_id);

CREATE INDEX idx_actor_roles_actor_id ON actor_roles(actor_id);

CREATE INDEX idx_tasks_employee_id ON tasks(employee_id);