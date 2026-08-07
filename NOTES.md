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

#### What FastAPI module provides a client for testing API endpoints?

The fastapi.testclient module provides the TestClient class for testing API endpoints

#### What command ensures all project dependencies are installed and synchronized after switching to a new branch?

The uv sync command ensures all dependencies specified in the project configuration are installed and synchronized

#### What are the main advantages of using SQLModel over SQLAlchemy directly?

SQLModel provides built-in Pydantic data validation while using SQLAlchemy under the hood, combining the best of both worlds. This prevents code duplication and eliminates the extra step of wiring in Pydantic validation separately.

#### In SQLMOdel, why would the id field of a model be defined as int | None with a default of None?

The id field can be None when a record has not been saved to the database yet. Once saved, the database will assign an id value, but before that point, the object exists without an id.

```python
from sqlmodel import SQLModel, Field

class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    author: str
    pages: int | None = Field(default=None)
```

#### How do you convert a Python class into a SQLModel table that can be used to communicate with a database?

Inherit from SQLModel and set the flag table=True in the class definition. This tells SQlModel that the class should be used to translate into a database table, not just for data validation.

#### In SQLModel, what is the difference between using SQLModel's field versus Pydantic's field?

When working with SQLModel classes that map to database tables, you should use SQLModel's field function rather than Pydantic's field function. SQLModel's field supports database specific configuration like setting contraints (e.g., unique = True) and column definitions that are needed for database operations, while still maintaining compatibility with Pydantic's validation features.

#### What does setting unique=True on a database field accomplish in SQLModel?

Setting unique=True creates a database constraint that ensures no two records can have the same value for that field. This prevents duplicates and can cause a conflict if an attempt is made to insert a duplicate value.

#### Why would you create separate schema classes for create, read, and update operations in SQLModel?

Different operations require different fields. For create operatios, the database generates values like ID and timestamps. For read operations, all fields including ID and timestamps are populated. For update operations, fields may be optional. This separation ensures each operation only includes the appropriate data.

#### What is the purpose of using a default_factory with a utc_now function for a created_at field in SQLModel?

The default_factory with utc_now automatically sets the current UTC timestamp when a new database row is created, without requiring manual input. This ensures consistent timezone handling and automatic timestamp creation.

#### What is the purpose of Alembic in database management?

Alembic is used for databse migrations. It creates revisions that tell you how to move the database forward (and sometimes backward), allowing you to have a snapshot of your database at each version. This lets you easily review and modify your database schema to match your Python models without manual work.

#### What two key pieces of information does Alembic need to know to function properly?

Alembic needs to know how to connect to the database and how to find the SQL model definitions.

#### What is the purpose of the env.py file in an Alembic setup?

env.py is the PYthon script that runs every time Alembic executes a command. It needs to know here the database URL is set in the config, import the SQLModel metadata, and ensure that SQLModel is imported (which is not done by default).

#### What does the alembic revision --autogenerate command do?

This command inspect the database schema, identifies what has changed, and automatically generates a migration revision file based on those changes.

#### What does the alembic upgrade head command accomplish?

This command takes any pending migration scripts and applies them to the database, updating the database schema to match the current state of the models.

#### What is dependency injection in FastAPI and how does it relate to database sessions?

Dependency injection in FastAPI is a mechanism where the framework calls a function before an endpoint runs and passes the result into the endpoint. For database sessions, FastAPI uses the Depends function to inject a session directly into route handlers, ensuring that each endpoint has access to a database session when needed.

#### How SALAlchemy/SQLModel handle the **get** method when a record is not found?

SQLAlchemy and SQLMOdel's **get** method returns None when nothing is found, rather than raising an exception

#### When using SQLModel's **one()** method for queries, what two exceptions can be raised?

The **one()** method will raise an exception in two cases: 1) If no results are found matching the query, it will raise a 'no result found' exception, and 2) if more than one result is found, it will raise an exception indicating that multiple matches were found when only one was expected.

#### How do you create a basic select statement in SQLModel to retrieve all projects ordered by name?

Use **select(Project).order_by(Project.name)** to create a select statement that retrieves all projects ordered by their name. The select function is imported from SQLModel, and the statement can then be executed using **session.exec()**

#### What is the purpose of the Annotated type hint when working with FastAPI dependencies?

The **Annotated** type hint in FastAPI is used to make function signatures cleaner and more descriptive. It combines the type information with dependency injection metadata, allowing you to specify both the type (like Session) and how it should be obtained (using Depends) in a single, readable annotation.

#### What is the purpose of calling session.refresh(project) after committing a new project to the database?

To refresh the project from the session and ensure that generated values like the primary key ID are available on the model instance. Without refereshing, the ID would not be set on the object.

#### What does the exlude_unset flag do when getting updated fields from a model in FastAPI?

It excludes fields that haven't been changed, returning only the fields that have actually been updated rather than all fields including unchanged ones.

#### What is the purpose of the depends function in FastAPI?

The depends function tells the framework to run a specified function before executing an endpoint and provide its result to the endpoint. It's used for dependency injection.

#### What is the primary purpose of using the Depends function in FastAPI?

To tell the framework to run another function first and provide its result before executing the endpoint

#### What happens when FastAPI resolves a dependency that uses a generator function iwth a yield statement?

It executes code until the yield, pauses for the route handler, then resumes after

#### How does SQLModel's context manager handle exceptions that occurs inside a **with** block?

It automatically rolls back uncommitted transactions

#### What type of error should be caught to handle duplicate project names or slugs in the database?

IntegrityError

#### What is the purpose of creating a dependencies.py file?

To organize reusable dependencies instead of keeping them in main.py

#### What HTTP status code should be returned when a request cannot be completed because it conflicts with existing data in the database?

409 (Conflict) is the status code that indicates a request cannot be completed because it conflicts with something else in the database.

#### Whcih SQLAlchemy exception is raised when a unique constraint is violated in the database?

IntegrityError

#### Why should HTTPException not be imported in the CRUD layer

The data layer should focus on database exceptions, while the web layer handles HTTP responses.

#### What is the purpose of APIRouter in FastAPI?

APIRouter helps split a FastAPI application into different routes or paths as smaller focused modules, which can then be merged or referenced back in the main file. This prevents all endpoint from being in one file and makes the application easier to navigate as it grows.
