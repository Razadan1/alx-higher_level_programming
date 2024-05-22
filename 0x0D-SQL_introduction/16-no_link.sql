-- lists all records of the table
INSERT INTO second_table(name, score) VALUES("Aria", 18),
("Aria", 12);
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
