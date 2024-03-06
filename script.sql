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

CREATE TABLE sections (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hall_id INTEGER NOT NULL,
    name VARCHAR(255) NOT NULL,
    seats INTEGER NOT NULL,
    FOREIGN KEY (hall_id) REFERENCES halls(id)
);

CREATE TABLE seats (
    seat_number INTEGER NOT NULL,
    hall_id INTEGER NOT NULL,
    section_id INTEGER,
    PRIMARY KEY (seat_number, hall_id, section_id),
    FOREIGN KEY (section_id) REFERENCES sections(id),
    FOREIGN KEY (hall_id) REFERENCES halls(id)
);

CREATE TABLE plays (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    hall_id INTEGER NOT NULL,
    FOREIGN KEY (hall_id) REFERENCES halls(id)
);