-- lists all cities contained in the database hbtn_0d_usa
SELECT cities.id, cities.name, states.name
FROM hbtn_0d_usa.cities
JOIN states ON cities.states.id = states.id
ORDER BY cities.id;
