-- Lists all records with a score >= 10 in second_table
-- ordered by score with their name next to them
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;