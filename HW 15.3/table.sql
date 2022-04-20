CREATE TABLE animal_breed (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE animal_color (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE animal_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL
);


CREATE TABLE outcome_subtype (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE outcome_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE new_animals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    animal_id VARCHAR(10) NOT NULL,
    age_upon_outcome VARCHAR(50) NOT NULL,
    name VARCHAR(50),
    date_of_birth TEXT NOT NULL,
    outcome_month INTEGER NOT NULL,
    outcome_year INTEGER NOT NULL,
    type_id INTEGER NOT NULL, FOREIGN KEY (type_id) REFERENCES animal_type(id),
    breed_id INTEGER NOT NULL, FOREIGN KEY (breed_id) REFERENCES animal_breed(id),
    color1_id INTEGER, FOREIGN KEY (color1_id) REFERENCES animal_color(id),
    color2_id INTEGER, FOREIGN KEY (color2_id) REFERENCES animal_color(id),
    outcome_type_id INTEGER, FOREIGN KEY (outcome_subtype_id) REFERENCES outcome_subtype(id),
    outcome_subtype_id INTEGER, FOREIGN KEY (outcome_type_id) REFERENCES outcome_type(id)
);