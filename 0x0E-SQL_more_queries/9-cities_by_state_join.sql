-- Lists all cities contained in the database 
SELECT cities.id , cities.name, states.name FROM cities JOIN states ON cities.name = states.name ORDER BY cities.id ASC;
