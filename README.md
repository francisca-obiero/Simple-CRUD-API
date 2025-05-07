 # Simple Contact Book CRUD API with FastAPI and MySQL

## Project Overview

This project implements a simple Contact Book API using FastAPI (Python framework) connected to a MySQL database. It demonstrates the creation of a fully functional CRUD (Create, Read, Update, Delete) API that manages contacts and groups, including their many-to-many relationships.

---
## Assignment Objective
Question 2: Create a Simple CRUD API Using MySQL + Programming

- Combine MySQL skills with a programming language (Python)
- Design a database schema with at least 2–3 tables
- Build an API using FastAPI
- Implement all CRUD operations (Create, Read, Update, Delete)
- Connect the API to the MySQL database

## What Has Been Done

### 1. SQL Script (`contactBook` Database)

- Created a database named `contactBook`.
- Designed three tables:
  - `contacts`: stores contact information (`id`, `name`, `email`, `phone`).
  - `groupsTable`: stores groups (`id`, `name`).
  - `contactGroups`: join table to represent many-to-many relationships between contacts and groups (`contactId`, `groupId`).
- Established foreign key constraints with cascading deletes to maintain referential integrity.

---

### 2. Pydantic Models (`schemas.py`)

- Defined data validation and serialization models using Pydantic:
  - `ContactBase`, `ContactCreate`, and `Contact` for contacts.
  - `GroupBase`, `GroupCreate`, and `Group` for groups.
  - `ContactWithGroups` to represent a contact with associated groups (for potential nested responses).
- Models ensure input data correctness and provide clear API schema definitions.

---

### 3. FastAPI Application (`main.py`)

- Connected to the MySQL database using `mysql.connector`.
- Implemented full CRUD endpoints for **contacts**:
  - `GET /contacts`: List all contacts.
  - `POST /contacts`: Create a new contact.
  - `PUT /contacts/{contactId}`: Update an existing contact.
  - `DELETE /contacts/{contactId}`: Delete a contact.
- Implemented full CRUD endpoints for **groups**:
  - `GET /groups`: List all groups.
  - `POST /groups`: Create a new group.
  - `PUT /groups/{groupId}`: Update an existing group.
  - `DELETE /groups/{groupId}`: Delete a group.
- Used Pydantic models for request validation and response serialization.
- Included error handling for common cases like missing records or database errors.
- Followed camelCase naming convention consistently in function names and path parameters.

---

## How to Run the Project

1. Set up MySQL database:
2. Install dependencies
3. Run the FastAPI server:
4. Access API documentation
   

## Project Structure

├── main.py        # FastAPI app with CRUD endpoints
├── schemas.py     # Pydantic models for data validation
└── contactBook.sql  # SQL script to create database and tables


