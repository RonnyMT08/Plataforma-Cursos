CREATE DATABASE IF NOT EXISTS cursosdb;

USE cursosdb;

CREATE TABLE IF NOT EXISTS Curses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT NOT NULL,
    created_at DATETIME NOT NULL
);

