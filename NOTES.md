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

#### Why is logging preffered over print statements in production code?

Logging is preferred in production because print statements can expose client data, secrets, or other sensitive information in logs, Many production codebases include CI/CD checks to prevent print statements from being deployed. Logging provides better control over what information is captured and how it's formatted.

#### What is the convention for naming a logger object in Python, and why is this convention used?

The convention is to use the special name variable when creating a logger with logging.getLogger(name). This automatically sets the logger name to the module's path, creating a hierarchy that allows for different logging configurations to flow down to different modules.

#### What are the five standard log level in Python's logging module, ordered from least to most server

Debug (detailed diagnostic info), Info(general operational events), Warning(something unexpected but non-critical happened), Error(serious problem affecting operations), Critical(most severe, critical system errors)

#### What is the purpose of using environment variables to control logging levels in Python applications?

Environment variables allow different logging levels to be used in different environments. For example, debug messages can be shown when running locally by setting DEBUG=true, while production environments can use info level logging to avoid surfacing debug messages.

#### What information is typically included in production log formats beyond just the log message?

Production log formats typically include timestamps, the source module that generated the log, and the log level. This provides more context and makes logs more useful for debugging and monitoring.

#### In Python logging configuration, what is the difference between setting the level to 'debug' versus 'info'?

When the level is set to 'debug', all log messages including debug-level messages are displayed. When set to 'info', only info-level and higher priority messages (warning, error, critical) are shown, while debug messages are suppressed.

#### What is the primary advantages of the loguru library over Python's standard library logger?

Loguru wraps the standard library API in a more ergonomic interface, offering one simple import and sensible defaults. It has approximately 24,000 starts on GitHub and is recommended when the standard library logger becomes cumbersome to use.

#### What type of log output does the structlog library product?

Structlog produces structured JSON-style log records, which are easier to parse and analyze programmatically compared to plain text logs.

#### What is middleware and what role does it play in a web application?

Middleware is code that runs before and after every request that is processed by an application. It acts as a bridge between the client and the route handler, allowing you to intercept incoming request (for logging, authentication, modifying headers) before they reach route logic, and intercept outgoing responses before they're returned to the client.

#### How do you define middleware in FastAPI using a decorator?

Use the app.middleware decorator with the middleware type (e.g., "HTTP"), then define an async function that takes a request and call_next parameter. Inside the function, call response = await call_next(request) and return the response. Any code before this line runs pre-route, and any code after runs post-route.

#### In what order are multiple middlewares executed when handling requests and response?

For requests: middlewares are executed from last registered to first registered (if you register first_middleware then last_middleware, the execution is last_middleware -> first_middleware -> route). For responses: middlewares are executed from first registered to last registered (route -> first_middleware -> last_middleware).

#### Why must middleware always be defined as async functions in FastAPI?

Middleware must be async because FastAPI runs on an asyncio event loop, and call_next returns a coroutine that needs to be awaited to run the next middleware or route handler and build the response. Since await is only allowed inside async def functions, synchronous middleware cannot work as it has no way to await call_next and get the response back.

#### What is the purpose of the call_next function in middleware?

call_next is a function that passes the request down the chain to the next route handler or to the next middleware. When the route handler finishes, call_next returns the response object, allowing you to modify, change, or log it before it goes back to the user.

#### What happens when SQLMOdel sees a string enum annotated on a column?

SQLModel stores the value as a string and adds a database level constraint that will reject anything outside of the explicitly listed enum values.

#### What is the purpose of using the index=True parameter on a project_id foreign key column?

Setting index=True causes the database to build an index on that column, which makes lookups significantly faster. This is useful for columns that will be queried frequently, such as foreign key relationships.

#### How does the SQLModel relationship function enable navigation between related objects?

When both sides of a relationship are wired up correctly using the relationship function with back_populates, related objects can be navigated in Python code (like task.project and project.tasks) without writing any joined queries manually

#### Why does the type annotation for tasks: list[Task] work even though the Task class is defined later in the file?

In Python 3.7+, type annotations can be evaluated lazily (either through from **future** import annotations or as default behavior in later versions), which automatically provides forward references. This allows type annotations to reference classes defined later in the same file without requiring string literals or special handling.

#### What potential issue can arise when a response includes related data if eager loading is not properly implemented?

N+1 queries can become an issue. This occurs when the database is queried multiple times unnecessarily - once for the main entity and then once for each related entity, rather than loading all the data efficiently in a minimal number of queries

#### What are the three key SQLAlchemy query methods mentioned for building relational queries and filtering?

The three key methods are: where (for filtering conditions), join(for combining related tables), and selecinload(for eager loading related data to avoid N+1 query problems).

#### What is the purpose of creating a dependency like get_task_or_404 in a FastAPI application?

The dependency loads a task by ID and automatically raises a 404 HTTP exception if the task doesn't exist. This eliminates the need for additional error checking in routes that require a task to be present, making the code cleaner and more reusable.

#### What testing infrastructure components are mentioned for easing the testing process with database operations?

In-memory SQLite, the static pool pattern, and a fixture chain that builds sample data for each test run. This eliminates the need to manually create test data in each individual test.

#### What code smell is identified when the same code is copied and pasted wholesale?

Copying and pasting code wholesale is a signal that there is an opportunity to refactor or generalize the code. Thsi typically indicates duplication that could be eliminated through better abstractions.

#### How does selectinload solve the N+1 query problem in SQLAlchemy?

selectinload tells SQLAlchemy to fetch all related records in one extra query eagerly ahead of time, resulting in only 2 queries total regardless of the number of rows returned. The first query loads the main records, and the secodn query does an internal lookup using IDs from the first result to combine them. This way, related data is already in memory when accessed.

#### What is the difference between selectinload (or eager loading with a second query using WHERE ID IN) and joinedload in SQLAlchemy?

selectinload (or eager loading with WHERE ID IN) runs a second query with a WHERE ID IN clause and is best for one-to-many or many-to-many relationships, keeping the first query more compact. joinedload uses a left outer join to pull related rows in the same query and might be better for 1-to-1 relationship or smaller one-to-many sets where row duplication does'nt matter as much.

#### What are the two main advantages of using SQLite for testing instead of PostgreSQL?

Speed is the primary advantage - an in-memory SQLite database can be created in seconds, while spinning up PostgreSQL for every test run takes much longer. Additionally, when configured properly, every test can get its own isolated database, preventing tests from interfering with each other.

#### What are the limitations of using SQLite as a test database when the production database is PostgreSQL?

SQLite doesn't enforce some PostgreSQL-specific behaviors, including issues with native enum types and some constraint checks that don't work the same way. This means even with 100% test coverage, there will be gaps that could hide subtle bugs related to PostgreSQL interaction, since the underlying infrastructuer doesn't exactly match

#### What is the purpose of the SQLite path syntax with no file system path in the database configuration?

An empty path creates an in-memory database rather than one stored on the file system. Each new engine starts with an empty schema, ensuring there's no leftover state between test runs and eliminating the need to cleanup after each test.

#### What is StaticPool with check_same_thread=False necessary when configuring SQLite for testing with FastAPI?

This configuration keeps the in-memory database alive across multiple connections with SQLAlchemy and the FastAPI test client. Without this pool override, the database could vanish between connections, causing tests to fail with cryptic errors.

#### Waht is the purpose of the yield sytnax in a pytest fixture that provides a database session?

The yield syntax ensures that the session block opens before the test runs and closes when the test finishes. This triggers a rollback on any uncommitted transactions and frees up the connection, providing proper cleanup after each test.

#### What is the difference between authentication and authorization in API security?

Authentication is ocnfirming that the person sending a request is who they claim to be - it's about veriying identity. Authorization is focused on permissions - once identity is established, it determines which actions that person is allowed to take.

#### What are the two main approaches for API authentication in modern applications?

Single sign-on and OAuth 2, which delegates authentication to a third party like Google, GitHub, or Okta; and first party email and password, where the application stores and verifies hashed passwords itself.

#### What are the key tradeoffs between using a third-party authentication versus implementing first-party email and password authentication?

Third-party authentication (SSO/OAuth2) delegates authentication to providers like Google, GitHub, or Okta, which handle password storage, resets, and account recovery, removing credential security burden from your application, However, it requires third-party setup, may involve vendor costs, and needs configuration of callback URLs and provider-specific settings.

First-party email and password authentication is simpler to implement with no third-party setup, no vendor costs, and no callback URLs or provider-specific configuration. However, the tradeoff is that credential security becomes entirely your responsibility, and you must safely store hashed passwords yourself. In practice, rolling you own auth is often considered a poor choice, and managed identity providers are typically recommended for production environments.

#### What is a JWT token and why is it used in API authentication?

JWT (JSON Web Token) is a token that encodes information about the user and an expiration time. It is signed by the server and sent to the client after successful authentication. The client includes this token is subsequent requests, allowing the server to verify the signature and decode the user information to authorize protected requests.

#### Describe the 5-step authentication flow for a password-based API authentication system.

Regisration: user creates account with email and password, password is hashed before sorting in database. 2) Login: client POSTs email and plain text password to /auth/token. 3) Verification: server looks up user by email, hashes submitted password, and compares against stored hash. 4) Token generation: if match, server signs a JWT encoding user info and expiration, then sends it back. 5) Protected requests: client includes JWT in header, server verifies signature and decodes user ID to authorize the request.

#### Why should plain text passwords never be stored in a database?

Plain text passwords should never be stored because databases can be compromised through SQL injection, leaked backups, misconfigured cloud buckets, or other security breaches. Since many users reuse passwords across multiple sites, a leak can elad to account takeovers on other platforms.

#### What is the key characteristic of a cryptographic hashing function?

A cryptographic hashing function takes an input of any size and returns a fixed-sized string. It is one-way and cheap to compute, meaning it's easy to hash a password but computationally infeasible to reverse the hash back to the original password.

#### How does password salting affect the deterministic nature of hashing?

When a salt is used, the same password hashed twice will not necessarily produce the same output because a unique salt is typically generated for each operation. However, the system can still verify the password because modern hashing alrogrithms embed the salt whithin the hash output itself. During verification, the algorithm uses the embedded salt from the stored hash to hash the input password the same way, then compares the results to determine if the password is correct.

#### What is ARgon2id and hwy is it recommended for password hashing?

Argon2id is a password hashing algorithm that won the Password Hashing Competition in 2015. It is currently recommended for new applications and is the algorithm recommended by FastAPI. It is deliberately slow and memory-intensive to make brute force attacks less effective.

#### What is the purpose of the get_password_hash() function in password security implementation?

The get_password_hash() function creates a hash from a plain text password that will be stored in the database. It uses the password hashing algorithm (such as Argon2id) to generate a secure hash that represents the password without storing the actual password.

```python
uv run python -c "import secrets; print(secrets.token_urlsafe(32))"
```

#### What are the three characteristics that an authentication token msut have?

The token msut be: 1) cheap to verify, 2) hard to forge, and 3) self-contained.

#### What are the three steps required when verifying a JWT token?

Decode the token with the signing key, 2) Pull the sub (subject claim) out of the payload, and 3) Look up that user in the database. If any of these steps fail, a 401 unauthorized error should be returned.

#### What does the OAuth2PasswordBearer utility from FastAPI automatically do when added to a route?

It tells FastAPI to expect a token in a specific format in the header. FastAPI will automatically pull the token out of the header on protected routes, reject requests without a token with a 401 status, and add an 'Authorize' button to the interactive docs UI that handles token generation and storage for subsequent requests.

#### What are the two specific exceptions that should be caught when decoding a JWT token?

nvalidTokenError from jwt.exceptions and ValueError. InvalidTokenError handles JWT-specific validation failures, while ValueError catches issue with types or other validation problems.

#### When validating an authenticated user, what two conditions should cause a credentials exception to be raised after successfully retrieving the user from the database?

A credential exception should be raised if the user is None (doesn't exist) or if the user is not active.

Using the same generic credentials exception for all failure points prevent exposing specific reason why authentication failed. This improves security by not revealing whether the token was malformed, expired, the user doesn't exists, or other specific details that could be useful to attackers.
