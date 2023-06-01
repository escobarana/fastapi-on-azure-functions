from pydantic import BaseModel

"""
Contains all schemas alias domain models of the application.
For domain modelling, the library pydantic is used.
Pydantic allows to create versatile domain models and ensures data integrity and much more.
"""


class ContactBase(BaseModel):
    """
    Contact base schema
    """

    FullName: str = None
    EmailAdressExternal: str = None
    FirstName: str = None
    LastName: str = None
    isExternalAccount: str = None
    Company: str = None

    class Config:
        fields = {
            "FullName": {"description": "Full name of the contact"},
            "EmailAdressExternal": {
                "description": "External email address of the contact"
            },
            "FirstName": {"description": "First name of the contact"},
            "LastName": {"description": "Last name of the contact"},
            "isExternalAccount": {"description": "Is the contact an external account?"},
            "Company": {"description": "Company of the contact"},
        }


class Contact(ContactBase):
    """
    Contact schema, database representation
    """

    Contact_Id: str

    class Config:
        fields = {
            "Contact_Id": {"description": "Unique ID of the contact"},
        }
