# NOTES

#### What are the two main technologies that FastAPI is built on top of?

FastAPI is built on top of Starlette (a web framework) and Pyndantic. These underlying technologies contribute to FastAPI being one of the fastest Python frameworks available

#### What automatic documentation features does FastAPI provide out of the box?

FastAPI provides automatic OpenAPI integration, which generates a Swagger UI and a ReDoc page for the API without requiring any additional configuration or manual specification writing. These interactive documentation pages allow testing API endpoints directly in the browser.

#### What is the difference between using fastapi dev and fastapi run commands?

fastapi dev is used for development environments and provides colorized terminal output, a better developer experience, and supports live reloading when code changes are detected. fastapi run is used for production environments.

#### In FastAPI, how do you define a GET endpoint that returns a list of dictionaries?

use the @app.get() decorator with the desired path (e.g., /projects), define a function with type hints for the return value, and return the Python data structure. FastAPI automatically converts the Python dictionary to a JSON response.

#### When should you use async def instead of def for FastAPI endpoints?

Use async def when your endpoint needs to await other asynchronous operations such as database calls, network requests, or third-party API calls. Regular def functions are automatically run by FastAPI in an external thread pool and won't block the main event loop.

#### What is the purpose of setting a response_model parameter in a FastAPI route decorator?

The response_model parameter serves three purposes: 1) It filters the response data to match the specified Pydantic model (removing any fields not in the model, like secret fields), 2) It validates the response data, and 3) It generates OpenAPI documentation for the enpoint, showing the expected response structure.

#### What is the difference between a path parameter and a query parameter in FastAPI?

A path parameter is part of the URL path itself, defined with curly braces like /projects/{project_id}, and is required for the route to match. A query parameter is an optional parameter added to the function signature with a default value (often None), accessed via the URL query string like /projects?name=value.

#### What are the two built-in documentation endpoints available in FastAPI, and what are their purposes?

FastAPI provides two built-in documentation endpoints: 1) /docs - an interactive Swagger UI interface where you can test API endpoints directly, and 2) /redoc - a ReDoc interface that displays API specifications with samples, expected inputs, and possible responses in a more traditional API documentation format.

#### When defining a Pydantic model by inheriting from BaseModel, how do you specify field types?

Field types are specified using type annotations. For example:

```python
class ProjectRead(BaseModel):
    id: int
    name: str
    slug: str
```

Each field is defined with its name followed by a colon and its type.
