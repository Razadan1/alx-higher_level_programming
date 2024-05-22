-- lists all records of the table
INSERT INTO second_table(name, score) VALUES("Aria", 18),
("Aria", 12);
SELECT score, name FROM second_table ORDER BY score DESC;
