from fastapi import FastAPI, HTTPException, status
from typing import List
import mysql.connector
from schemas import ContactCreate, Contact, GroupCreate, Group, ContactWithGroups

app = FastAPI()

# Function to create and return a new database connection
def getDbConnection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="##Ombuds@25#",
        database="contactBook",
    )

# --- CONTACTS CRUD ENDPOINTS ---

# Get all contacts
@app.get("/contacts", response_model=List[Contact])
def readContacts():
    connection = getDbConnection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    cursor.close()
    connection.close()
    return contacts

# Create a new contact
@app.post("/contacts", response_model=Contact, status_code=status.HTTP_201_CREATED)
def createContact(contact: ContactCreate):
    connection = getDbConnection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            "INSERT INTO contacts (name, email, phone) VALUES (%s, %s, %s)",
            (contact.name, contact.email, contact.phone)
        )
        connection.commit()
        contact_id = cursor.lastrowid
        cursor.close()
        connection.close()
        # Return the created contact with its new ID
        return Contact(id=contact_id, **contact.dict())
    except mysql.connector.Error as err:
        cursor.close()
        connection.close()
        raise HTTPException(status_code=400, detail=str(err))

# Update an existing contact by ID
@app.put("/contacts/{contactId}", response_model=Contact)
def updateContact(contactId: int, contact: ContactCreate):
    connection = getDbConnection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM contacts WHERE id = %s", (contactId,))
    existing = cursor.fetchone()
    if not existing:
        cursor.close()
        connection.close()
        raise HTTPException(status_code=404, detail="Contact not found")
    cursor.execute(
        "UPDATE contacts SET name = %s, email = %s, phone = %s WHERE id = %s",
        (contact.name, contact.email, contact.phone, contactId)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return Contact(id=contactId, **contact.dict())

# Delete a contact by ID
@app.delete("/contacts/{contactId}", status_code=status.HTTP_204_NO_CONTENT)
def deleteContact(contactId: int):
    connection = getDbConnection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM contacts WHERE id = %s", (contactId,))
    existing = cursor.fetchone()
    if not existing:
        cursor.close()
        connection.close()
        raise HTTPException(status_code=404, detail="Contact not found")
    cursor.execute("DELETE FROM contacts WHERE id = %s", (contactId,))
    connection.commit()
    cursor.close()
    connection.close()
    return

# --- GROUPS CRUD ENDPOINTS ---

# Get all groups
@app.get("/groups", response_model=List[Group])
def readGroups():
    connection = getDbConnection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM groupsTable")
    groups = cursor.fetchall()
    cursor.close()
    connection.close()
    return groups

# Create a new group
@app.post("/groups", response_model=Group, status_code=status.HTTP_201_CREATED)
def createGroup(group: GroupCreate):
    connection = getDbConnection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            "INSERT INTO groupsTable (name) VALUES (%s)",
            (group.name,)
        )
        connection.commit()
        group_id = cursor.lastrowid
        cursor.close()
        connection.close()
        # Return the created group with its new ID
        return Group(id=group_id, **group.dict())
    except mysql.connector.Error as err:
        cursor.close()
        connection.close()
        raise HTTPException(status_code=400, detail=str(err))

# Update an existing group by ID
@app.put("/groups/{groupId}", response_model=Group)
def updateGroup(groupId: int, group: GroupCreate):
    connection = getDbConnection()
    cursor = connection.cursor()
