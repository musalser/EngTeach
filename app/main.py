from fastapi import FastAPI
import logging
from app.api.v1.api import api_router


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

# Include routers
app.include_router(api_router)
