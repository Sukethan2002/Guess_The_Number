CREATE DATABASE guess_game_db;

USE guess_game_db;

CREATE TABLE game_results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    tries INT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
