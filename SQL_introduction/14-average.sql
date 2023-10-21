-- Collects the average score
-- from second_table
ALTER TABLE second_table
ADD average INT;
SELECT AVG(score)
FROM second_table;