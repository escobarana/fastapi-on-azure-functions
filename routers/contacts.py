import logging
from typing import List, Optional

from fastapi import APIRouter, Depends

import schemas
from dependencies import get_db
from orm import DatabaseManagerBase
from utilities.exceptions import EntityNotFoundException

router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.get(
    "/",
    response_model=Optional[List[schemas.Contact]],
    summary="Retrieves all contacts",
    description="Retrieves all available contacts from the API",
)
async def read_contact(db: DatabaseManagerBase = Depends(get_db)):
    logging.debug("Contacts: Fetch contacts")
    contacts = db.get_contacts()
    return contacts


@router.get(
    "/{company_name}",
    response_model=Optional[List[schemas.Contact]],
    summary="Retrieve contacts by company name",
    description="Retrieves contacts by company name, if no company matches the filter criteria a 404 error is returned",
)
async def read_contact(company_name: str, db: DatabaseManagerBase = Depends(get_db)):
    logging.debug("Contact: Fetch contacts by company name")
    contacts = db.get_contacts_company(company=company_name)
    if contacts is None or len(contacts) == 0:
        raise EntityNotFoundException(
            code="Unable to retrieve contacts",
            description=f"No contacts with company name '{company_name}'",
        )
    return contacts
