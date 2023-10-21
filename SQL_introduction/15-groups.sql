-- Lists the number of records with the same score
-- from second_table
SELECT COUNT(score) AS 'number'
FROM second_table
GROUP BY score;