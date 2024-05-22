-- Diplays the top 3 cities temperature during July and August
-- ordered by temperature 
SELECT city, AVG(value) as avg_temp FROM temperature WHERE month = 7 AND 8 ORDER BY avg_temp DESC;
