CREATE DATABASE IF NOT EXISTS secureapp;
USE secureapp;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    role VARCHAR(20) NOT NULL
);

INSERT INTO users (username, password, email, role) VALUES
('admin', 'admin123', 'admin@example.com', 'admin'),
('ricardo', 'pass123', 'ricardo@example.com', 'user'),
('maria', 'maria123', 'maria@example.com', 'user'),
('guest', 'guest', 'guest@example.com', 'guest');
