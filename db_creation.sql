CREATE DATABASE cinema_manager;

use cinema_manager;

CREATE TABLE customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL,
    birthdate DATE NOT NULL,
    movie_code VARCHAR(255) NOT NULL
);

CREATE TABLE movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_code VARCHAR(255) NOT NULL,
    title VARCHAR(255) NOT NULL,
    release_date DATE NOT NULL,
    genres VARCHAR(255) NOT NULL,
    duration INT NOT NULL
);
