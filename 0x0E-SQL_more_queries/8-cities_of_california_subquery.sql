-- Lists all the cities fo California that can be found in the database
SELECT id INTO @california_id FROM states WHERE name = 'California';
SELECT id, name FROM states WHERE name = @california_id ORDER BY id ASC;
