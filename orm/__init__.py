from abc import ABC, abstractmethod
from typing import Optional, List

import schemas


class DatabaseManagerBase(ABC):
    """
    Example implementation of a database manager.
    In a productive application, SQLAlchemy or another ORM framework could be used here (depending on the database used).
    This is a very simplified database manager for demonstration purposes.
    """

    @abstractmethod
    def get_contacts(self) -> Optional[List[schemas.Contact]]:
        """
        Returns all contacts from the database
        Returns:
            Optional[List[schemas.Contact]]: List of contacts
        """
        ...

    @abstractmethod
    def get_contacts_company(self, company: str) -> Optional[schemas.Contact]:
        """
        Returns specific contacts by company
        Args:
            company (str): name of the company

        Returns:
            Optional[schemas.Contact]: Returns the specified contact
        """
        ...


class FakeDataBaseManager(DatabaseManagerBase):
    def __init__(self) -> None:
        super().__init__()

        self._contacts = [
            schemas.Contact(
                Contact_id=1,
                FullName="FullName 1",
                EmailAdressExrernal="contact1@imec.be",
                FirstName="FirstName 1",
                LastName="LastName 1",
                isExternalAccount="No",
                Company="Company 1",
            ),
            schemas.Contact(
                Contact_id=2,
                FullName="FullName 2",
                EmailAdressExrernal="contact2@imec.be",
                FirstName="FirstName 2",
                LastName="LastName 2",
                isExternalAccount="No",
                Company="Company 2",
            ),
            schemas.Contact(
                Contact_id=3,
                FullName="FullName 3",
                EmailAdressExrernal="contact3@imec.be",
                FirstName="FirstName 3",
                LastName="LastName 3",
                isExternalAccount="No",
                Company="Company 3",
            ),
        ]

    def get_contacts(self) -> Optional[List[schemas.Contact]]:
        return self._contacts

    def get_contacts_company(self, company: str) -> Optional[schemas.Contact]:
        return next(iter([p for p in self._contacts if p.Company == company]), None)