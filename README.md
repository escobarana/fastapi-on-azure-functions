---
page_type: sample
languages:
- python
products:
- azure
- azure-functions
description: "This is a sample Azure Function app created with the FastAPI framework."
title: Using FastAPI Framework with Azure Functions
author: escobarana
urlFragment: azure-functions-python-create-fastapi-app
---

# Using FastAPI Framework with Azure Functions

Azure Functions supports WSGI and ASGI-compatible frameworks with HTTP-triggered Python functions. This can be helpful if you are familiar with a particular framework, or if you have existing code you would like to reuse to create the Function app. The following is an example of creating an Azure Function app using Fast API.

## Prerequisites

You can develop and deploy a function app using either Visual Studio Code or the Azure CLI. Make sure you have the required prerequisites for your preferred environment:

* [Prerequisites for VS Code](https://docs.microsoft.com/azure/azure-functions/create-first-function-vs-code-python#configure-your-environment)
* [Prerequisites for Azure CLI](https://docs.microsoft.com/azure/azure-functions/create-first-function-cli-python#configure-your-local-environment)

## Setup

Clone or download [this sample's repository](https://github.com/escobarana/fastapi-on-azure-functions/), and open the `fastapi-on-azure-functions` folder in Visual Studio Code or your preferred editor (if you're using the Azure CLI).

## Using FastAPI Framework in an Azure Function App

The code in the sample folder has already been updated to support use of the FastAPI. Let's walk through the changed files.

The `requirements.txt` file has additional dependencies of the `fastapi` module:

```
azure-functions
fastapi
pydantic
pandas
```


The file host.json includes the a `routePrefix` key with a value of empty string.

```json
{
  "version": "2.0",
  "extensions": {
    "http": {
        "routePrefix": ""
    }
  }
}
```


Inside the `WrapperFunction` folder, the file `function.json` includes a `route` key in the bindings:

```json
{
  "scriptFile": "__init__.py",
  "bindings": [
    {
      "authLevel": "function",
      "type": "httpTrigger",
      "direction": "in",
      "name": "req",
      "methods": [
        "get"
      ],
      "route": "{*route}"
    },
    {
      "type": "http",
      "direction": "out",
      "name": "$return"
    }
  ]
}
```

* authLevel is set to `function` to require an API key to invoke the function. 
* The `route` key is set to `{*route}` to allow the function to handle all routes. 
* The `methods` key is set to `get` to allow the function to handle GET requests.

In that same folder, the `__init__.py` file uses `AsgiMiddleware` to redirect invocations to a FastAPI app with two routes defined.

## Running the sample

### Testing locally

First run the command below to install the necessary requirements.

```log
python3 -m pip install -r requirements.txt
```

If you are using VS Code for development, follow [the instructions for running a function locally](https://docs.microsoft.com/azure/azure-functions/create-first-function-vs-code-python#run-the-function-locally). Otherwise, follow [these instructions for using Core Tools commands directly to run the function locally](https://docs.microsoft.com/azure/azure-functions/functions-run-local?tabs=v4%2Cwindows%2Cpython%2Cportal%2Cbash#start).

Once the function is running, test the function at the local URL displayed in the Terminal panel:

```log
Functions:
        WrapperFunction: [GET,POST] http://localhost:7071/{*route}?code=<API_KEY>
```

Try out URLs corresponding to the handlers in the app, both the simple path and the parameterized path:

```
http://localhost:7071/contacts?code=<API_KEY>
http://localhost:7071/contacts/company_name?code=<API_KEY>
```

### Deploying to Azure

There are three main ways to deploy this to Azure:

* [Deploy with the VS Code Azure Functions extension](https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python#publish-the-project-to-azure). 
* [Deploy with the Azure CLI](https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=azure-cli%2Cbash%2Cbrowser#create-supporting-azure-resources-for-your-function).
* Deploy with the Azure Developer CLI: After [installing the `azd` tool](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/install-azd?tabs=localinstall%2Cwindows%2Cbrew), run `azd up` in the root of the project. You can also run `azd pipeline config` to set up a CI/CD pipeline for deployment.

### Testing in Azure

Once deployed, test different paths on the deployed URL, using either a browser or a tool like Postman.

```
http://<FunctionAppName>.azurewebsites.net/contacts?code=<API_KEY>
http://<FunctionAppName>.azurewebsites.net/contacts/company_name?code=<API_KEY>
```

If you get an error about `handle_async` not being defined, that is likely because the Azure Functions runtime doesn't yet have the latest version of `azure-functions`.
To work around that for now, add an environment value with the name `PYTHON_ISOLATE_WORKER_DEPENDENCIES` and value of `1`.
That environment variable ensures that the packages in your `requirements.txt` are installed in a separate virtual environment than the packages of the functions runtime.

## Conclusion and Next Steps

Now you have a simple Azure Function App using the FastAPI framework, and you can continue building on it to develop more sophisticated applications.

To learn more about leveraging WSGI and ASGI-compatible frameworks, see [Web frameworks](https://docs.microsoft.com/azure/azure-functions/functions-reference-python?tabs=asgi%2Cazurecli-linux%2Capplication-level#web-frameworks).
