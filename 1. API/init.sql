CREATE TABLE birthday (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
    birthdaydate DATE NOT NULL,
	CONSTRAINT constraint_name UNIQUE (name)
);