-- a script that lists all cities contained in the database hbtn_0d_usa.
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id
-- You can use only one SELECT statement
SELECT a.id AS id, a.name AS name, b.name AS name
FROM cities a
INNER JOIN states b ON a.state_id = b.id
ORDER BY a.id ASC;

