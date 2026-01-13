from fastapi import APIRouter
from datetime import datetime
import os

router = APIRouter()

@router.get("/health")
def health_check():
    """
    Basic health check endpoint.
    Used for monitoring, container orchestration, and uptime checks.
    """

    status = {
        "status": "ok",
        "service": "rag-document-assistant",
        "timestamp": datetime.utcnow().isoformat(),
        "environment": os.getenv("ENV", "development"),
        "checks": {
            "api": True,
            "llm": True,
            "vector_store": True
        }
    }

    return status
