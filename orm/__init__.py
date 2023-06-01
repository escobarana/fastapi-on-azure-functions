from abc import ABC, abstractmethod
from typing import List, Optional

import pandas as pd

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
    def get_contacts_company(self, company: str) -> Optional[List[schemas.Contact]]:
        """
        Returns specific contacts by company
        Args:
            company (str): name of the company

        Returns:
            Optional[List[schemas.Contact]]: List of contacts belonging to the given company
        """
        ...


class FakeDataBaseManager(DatabaseManagerBase):
    def __init__(self) -> None:
        super().__init__()
        source_contacts = pd.read_csv("resources/data.csv", delimiter=',')
        self._contacts = [
            schemas.Contact(
                Contact_Id=row["Contact_Id"],
                FullName=row["FullName"],
                EmailAdressExternal=row["EmailAdressExternal"],
                FirstName=row["FirstName"],
                LastName=row["LastName"],
                isExternalAccount=row["isExternalAccount"],
                Company=row["Company"],
            )
            for index, row in source_contacts.iterrows()
        ]

    def get_contacts(self) -> Optional[List[schemas.Contact]]:
        return self._contacts

    def get_contacts_company(self, company: str) -> Optional[List[schemas.Contact]]:
        return [p for p in self._contacts if p.Company == company]
