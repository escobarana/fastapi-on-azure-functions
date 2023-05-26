import azure.functions as func
from FastAPIApp import app  # Main API application


@app.get("/")
def index():
    return {
        "info": "Try /contacts or /contacts/company_name.",
    }


@app.get("/hello/{name}")
async def get_name(name: str):
    return {
        "name": name,
    }


async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return await func.AsgiMiddleware(app).handle_async(req, context)
