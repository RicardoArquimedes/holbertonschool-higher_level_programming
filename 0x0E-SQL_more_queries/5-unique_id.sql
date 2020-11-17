-- script that creates the table unique_id.
CREATE TABLE IF NOT EXISTS unique_id(
        id INT NULL DEFAULT 1 UNIQUE,
        name VARCHAR(256)
);