### A small FARM (FastAPI-React-MongoDB) boilerplate with Docker

- add this .env file in backend folder

```
PROJECT_NAME=backend
BACKEND_CORS_ORIGINS=["http://localhost:8000", "https://localhost:8000", "http://localhost", "https://localhost", "http://localhost:3000"]


DATABASE_URI=<your own database uri>
DB_NAME=<your own darabase name>

```
- add this .env file in frontend folder

```
FAST_REFRESH=false
REACT_APP_API_BASE_URL=<backend server url>

```
