#schemas.py
# from pydantic import BaseModel, EmailStr 

from pydantic import BaseModel, EmailStr
from typing import Optional, List

from typing import Optional, List

class ContactBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None

class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    id: int

    class Config:
        orm_mode = True

class GroupBase(BaseModel):
    name: str

class GroupCreate(GroupBase):
    pass

class Group(GroupBase):
    id: int

    class Config:
        orm_mode = True

class ContactWithGroups(Contact):
    groups: List[Group] = []
