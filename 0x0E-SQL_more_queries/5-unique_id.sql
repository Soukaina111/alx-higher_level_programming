-- This script creates a table in the db with its attributes
CREATE table IF NOT EXISTS unique_id(id INT NOT NULL DEFAULT 1 UNIQUE, name VARCHAR(256));
