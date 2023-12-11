## FastAPI with JWT Token Authorization and Postgres DB

This project demonstrates how to build a FastAPI application with JWT token authorization and a Postgres database.

### Installation

1. Clone the repository: `git clone https://github.com/your-username/your-repo.git`
2. Navigate to the project directory: `cd your-repo`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
    - On Windows: `venv\Scripts\activate`
    - On macOS/Linux: `source venv/bin/activate`
5. Install the dependencies: `pip install -r requirements.txt`

### Configuration

1. Create a `.env` file in the project root directory.
2. Add the following environment variables to the `.env` file:

    ```plaintext
    DATABASE_URL=postgresql://username:password@localhost:5432/db_name
    SECRET_KEY=your-secret-key
    ```

### Usage

1. Run the application: `uvicorn main:app --reload`
2. Open your browser and navigate to `http://localhost:8000/docs` to access the Swagger UI documentation.
3. Use the provided endpoints to interact with the API.
