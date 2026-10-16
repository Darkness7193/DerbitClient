Requirements. Требования:
    git
    Mint Cinnamon or Ubuntu 22.04


Installation. Установка:

    git clone https://github.com/Darkness7193/DerbitClient DerbitClient

    uv sync &&
    mv example.env .env &&
    sudo docker compose up --build -d

    # Wait 5-15c. Подождать 5-15с

    sudo docker compose exec rabbitmq rabbitmqctl add_user rabbitmquser password &&
    sudo docker compose exec rabbitmq rabbitmqctl set_permissions -p / rabbitmquser ".*" ".*" ".*" &&
    sudo docker compose exec -it app uv run alembic upgrade head &&
    sudo docker compose up --build


Доступный API:

    1. Метод для тестов. Получает и сохраняет tickers_data объект:
        GET http://127.0.0.1:8000/fetch_ticker?ticker=BTC-PERPETUAL
        ticker: str. Название валюты. Список доступных значений можно узнать на
        https://docs.deribit.com/api-reference/market-data/public-get_instruments

    2. Получение всех сохраненных данных по указанной валюте:
        GET http://localhost:8000/get_all_currency_data?ticker=BTC-PERPETUAL
        ticker: str. Название валюты. Список доступных значений можно узнать на
        https://docs.deribit.com/api-reference/market-data/public-get_instruments

    3. Получение последней цены валюты:
        GET http://localhost:8000/get_last_currency_price?ticker=BTC-PERPETUAL
        ticker: str. Название валюты. Список доступных значений можно узнать на https://docs.deribit.com/api-reference/market-data/public-get_instruments

    4. Получение цены валюты с фильтром по дате:
        GET http://localhost:8000/get_currency_price?ticker=BTC-PERPETUAL&start_iso_date=2020-01-01T00:00:00Z
        ticker:         str.      Название валюты. Список доступных значений можно узнать на
            https://docs.deribit.com/api-reference/market-data/public-get_instruments
        start_iso_date: iso_date. Начальная дата фильтрования по датам
        end_iso_date:   iso_date. Конечная дата фильтрования по датам


Available API:

    1. Endpoint for testing. Fetches and saves a tickers_data record:
        GET http://127.0.0.1:8000/fetch_ticker?ticker=BTC-PERPETUAL
        ticker: str. The currency instrument name. Available values can be found at
        https://docs.deribit.com/api-reference/market-data/public-get_instruments

    2. Retrieve all saved data for a specified currency:
        GET http://localhost:8000/get_all_currency_data?ticker=BTC-PERPETUAL
        ticker: str. The currency instrument name. Available values can be found at
        https://docs.deribit.com/api-reference/market-data/public-get_instruments

    3. Retrieve the latest price of a currency:
        GET http://localhost:8000/get_last_currency_price?ticker=BTC-PERPETUAL
        ticker: str. The currency instrument name. Available values can be found at
        https://docs.deribit.com/api-reference/market-data/public-get_instruments

    4. Retrieve currency prices filtered by date:
        GET http://localhost:8000/get_currency_price?ticker=BTC-PERPETUAL&start_iso_date=2020-01-01T00:00:00Z
        ticker: str. The currency instrument name. Available values can be found at
            https://docs.deribit.com/api-reference/market-data/public-get_instruments
        start_iso_date: ISO 8601 date-time. The start date for filtering the data.
        end_iso_date: ISO 8601 date-time. The end date for filtering the data.


Design Decisions

    1. Python Dependency Management
        The project uses uv for dependency management and virtual environment handling. Dependencies are declared in pyproject.toml with minimum version constraints (>=), allowing compatible newer versions to be installed.

    2. FastAPI for the Application Layer
        FastAPI is used to build the application's HTTP API. It provides request validation, automatic API documentation, and integration with Pydantic models. Uvicorn serves the application as the ASGI server.

    3. Asynchronous I/O
        Asynchronous libraries are used where appropriate to improve I/O efficiency. aiohttp handles asynchronous HTTP requests to the Deribit API, while SQLAlchemy's asyncio support and asyncpg provide asynchronous database access.
        This approach allows the application to handle network and database operations without unnecessarily blocking the event loop.

    4. Deribit API Integration
        The application retrieves market data from the Deribit API using HTTP requests. aiohttp is used for asynchronous requests, while requests remains available for synchronous HTTP operations where needed.
        Separating external API communication from data persistence makes the code easier to maintain and test.

    5. PostgreSQL as the Database
        PostgreSQL is used for persistent storage of ticker data. It provides reliable relational storage and supports structured queries for historical market data.
        The asyncpg driver is used for asynchronous database operations, while psycopg[binary] supports synchronous PostgreSQL connections and tools that require the Psycopg driver.

    6. SQLAlchemy as the ORM
        SQLAlchemy is used to define database models and manage database operations. Its ORM maps Python objects to relational database records, reducing the need to write raw SQL for routine operations.
        The asynchronous SQLAlchemy interface is used for database operations in asynchronous application code.

    7. Alembic for Database Migrations
        Alembic manages database schema changes through version-controlled migration scripts. This makes schema updates reproducible and helps keep the database structure consistent across development and deployment environments.

    8. Celery for Background Tasks
        Celery is used to execute background tasks independently of HTTP request handling. Periodic ticker collection can be scheduled to retrieve market data at regular intervals without blocking the API.
        This separation improves maintainability and allows background processing to scale independently.

    9. RabbitMQ as the Message Broker
        RabbitMQ is used as the message broker between the application and Celery workers. It transports task messages and decouples task submission from task execution.
        This architecture allows workers to process tasks independently of the API service.

    10. Pydantic Settings for Configuration
        pydantic-settings is used to load and validate application configuration, including database credentials, connection URLs, and external service settings.
        Environment variables and environment files keep configuration separate from application code and help avoid hardcoding credentials.

    11. Docker Integration
        The Docker Python SDK is available for interacting with Docker programmatically. Containerization provides a consistent runtime environment and simplifies running application services and dependencies together.

    12. Type Safety and Maintainability
        celery-types provides type information for Celery, improving static analysis and editor support. Type annotations and clearly separated application components help make the code easier to understand, maintain, and extend.

    13. Separation of Responsibilities
        The application separates HTTP endpoints, external API communication, background task execution, database models, and configuration into distinct components. This modular structure reduces coupling and makes individual components easier to test and replace.
