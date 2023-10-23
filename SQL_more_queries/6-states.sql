-- Creates the database hbtn_0d_usa and the table states
-- id is UNIQUE, AUTO GEN, NOT NULL (& name), and id is primary key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE AUTO_INCREMENT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);