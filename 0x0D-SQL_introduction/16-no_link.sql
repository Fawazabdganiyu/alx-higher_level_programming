-- LIsts all the records of the table in a format.
SELECT score, `name`
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
