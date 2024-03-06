CREATE TABLE theatres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
);

CREATE TABLE halls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    seats INTEGER NOT NULL,
    theatre_id INTEGER NOT NULL,
    FOREIGN KEY (theatre_id) REFERENCES theatres(id)
);

CREATE TABLE areas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hall_id INTEGER NOT NULL,
    name VARCHAR(255) NOT NULL,
    seats INTEGER NOT NULL,
    FOREIGN KEY (hall_id) REFERENCES halls(id)
);

CREATE TABLE seats (
    chair_number INTEGER NOT NULL,
    row_number INTEGER,
    hall_id INTEGER NOT NULL,
    area_id INTEGER,
    PRIMARY KEY (chair_number, row_number, hall_id, area_id),
    FOREIGN KEY (area_id) REFERENCES areas(id),
    FOREIGN KEY (hall_id) REFERENCES halls(id)
);

CREATE TABLE plays (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    hall_id INTEGER NOT NULL,
    FOREIGN KEY (hall_id) REFERENCES halls(id)
);

CREATE TABLE showings (
    play_id INTEGER NOT NULL,
    date DATE NOT NULL,
    PRIMARY KEY (play_id, date),
    FOREIGN KEY (play_id) REFERENCES plays(id)
);

CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    mobile_number VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL
);

CREATE TABLE tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    play_date_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    seat_id INTEGER NOT NULL,
    FOREIGN KEY (play_date_id) REFERENCES showings(play_id, date),
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (seat_id) REFERENCES seats(chair_number)
);

CREATE TABLE ticket_purchases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dato DATE NOT NULL,
    ticket_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE TABLE tickets_in_purchase (
    ticket_purchase_id INTEGER NOT NULL,
    ticket_id INTEGER NOT NULL,
    PRIMARY KEY (ticket_purchase_id, ticket_id),
    FOREIGN KEY (ticket_purchase_id) REFERENCES ticket_purchases(id),
    FOREIGN KEY (ticket_id) REFERENCES tickets(id)
);

CREATE TABLE actors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE roles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE actor_roles (
    actor_id INTEGER NOT NULL,
    role_id INTEGER NOT NULL,
    play_id INTEGER NOT NULL,
    PRIMARY KEY (actor_id, role_id, play_id),
    FOREIGN KEY (actor_id) REFERENCES actors(id),
    FOREIGN KEY (role_id) REFERENCES roles(id),
    FOREIGN KEY (play_id) REFERENCES plays(id)
);

CREATE TABLE acts (
    play_id INTEGER NOT NULL,
    number INTEGER NOT NULL,
    name VARCHAR(255),
    PRIMARY KEY (play_id, number),
    FOREIGN KEY (play_id) REFERENCES plays(id)
);

CREATE TABLE role_acts (
    role_id INTEGER NOT NULL,
    act_id INTEGER NOT NULL,
    PRIMARY KEY (role_id, act_id),
    FOREIGN KEY (role_id) REFERENCES roles(id),
    FOREIGN KEY (act_id) REFERENCES acts(id)
);

CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    employee_status VARCHAR(50) NOT NULL,
);

CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    play_id INTEGER NOT NULL,
    task VARCHAR(255) NOT NULL,
    employee_id INTEGER NOT NULL,
    FOREIGN KEY (play_id) REFERENCES plays(id),
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);

CREATE INDEX idx_theatre_id ON halls(theatre_id);

CREATE INDEX idx_hall_id ON areas(hall_id);

CREATE INDEX idx_area_id ON seats(area_id);

CREATE INDEX idx_hall_id_play_id ON plays(hall_id);

CREATE INDEX idx_play_id_customer_id ON tickets(play_id, customer_id);

CREATE INDEX idx_play_id_employee_id ON tasks(play_id, employee_id);