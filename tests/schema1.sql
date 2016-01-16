
CREATE TABLE people
(
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    home INTEGER,

    FOREIGN KEY(home) REFERENCES home(id)
);


CREATE TABLE cats
(
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    owner INTEGER NOT NULL,
    color TEXT,

    FOREIGN KEY(owner) REFERENCES people(id)
);


CREATE TABLE home
(
    id INTEGER PRIMARY KEY,
    address TEXT,
    zip_code INTEGER,
    state INTEGER,

    FOREIGN KEY(state) REFERENCES state(id)
);

CREATE TABLE state
(
    id INTEGER PRIMARY KEY,
    name TEXT
);



