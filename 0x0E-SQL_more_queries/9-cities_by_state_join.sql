-- This script select specific cities and states from db
SELECT cities.id, cities.name, states.name FROM cities, states
WHERE cities.state_id = states.id ORDER BY cities.id ASC;
