-- Creates a table called force_name
-- name cannot be null (empty)
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) IS NOT NULL
);