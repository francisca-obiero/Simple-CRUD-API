-- Create database contactBook
CREATE DATABASE contactBook;

-- Use the database
USE contactBook;

-- Create table contacts
CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20)
);

-- create new groups table
CREATE TABLE groupsTable (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

-- Join table for many-to-many relationship
CREATE TABLE contactGroups (
    contactId INT,
    groupId INT,
    PRIMARY KEY(contactId, groupId),
    FOREIGN KEY (contactId) REFERENCES contacts(id) ON DELETE CASCADE,
    FOREIGN KEY (groupId) REFERENCES groupsTable(id) ON DELETE CASCADE
);
