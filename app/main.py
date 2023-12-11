from fastapi import FastAPI
import logging
from app.api.v1.api import api_router
from fastapi.middleware.cors import CORSMiddleware


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log")
    ]
)


logger = logging.getLogger(__name__)

app = FastAPI()  # Create FastAPI instance

# Add CORS headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(api_router)
