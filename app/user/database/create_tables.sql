CREATE TABLE IF NOT EXISTS users (
    user_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR NOT NULL,
    email VARCHAR UNIQUE NOT NULL,
    password VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS user_preferences (
    preferences_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id INT,
    color INT NOT NULL,
    fuel INT NOT NULL,
    transmission INT NOT NULL,
    max_price INT NOT NULL
);