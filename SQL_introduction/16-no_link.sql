-- Lists all records of the table
-- only if there's a name
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;