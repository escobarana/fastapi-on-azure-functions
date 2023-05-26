from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from routers import contacts
from utilities.exceptions import ApiException

description = """
This is a sample API based on Azure Functions and FastAPI.

This API is used to illustrate how a potential API with Azure Functions and FastAPI could look like, it is a demo API only.

## Contacts
* Retrieve contacts
* Retrieve a specific contact by company name
"""

app = FastAPI(
    title="Azure Function Demo FastAPI",
    description=description,
    version="0.1",
    contact={
        "name": "Ana Escobar Llamazares",
        "url": "https://ana-escobar.com",
        "email": "anaescobar@ana-escobar.com",
    },
)
app.include_router(contacts.router)
# Add additional api routers here

@app.exception_handler(ApiException)
async def generic_api_exception_handler(request: Request, ex: ApiException):
    """
    Generic API exception handler.
    Ensures that all thrown excpetions of the custom type API Excpetion are returned
    in a unified exception JSON format (code and description).
    Args:
        request (Request): HTTP Request
        ex (ApiException): Thrown exception

    Returns:
        JSONResponse: Returns the exception in JSON format
    """
    return JSONResponse(
        status_code=ex.status_code,
        content={"code": ex.code, "description": ex.description},
    )
