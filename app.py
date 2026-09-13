import json
import logging
import uuid
from pathlib import Path
from typing import Any, Generator

from fastapi import FastAPI, HTTPException, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import FileResponse, HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
import uvicorn
from dotenv import load_dotenv

# ---------------------------------------------------------
# Import the existing compiled LangGraph workflow.
#
# backend.py remains completely unchanged.
# backend.app is the compiled LangGraph workflow.
# ---------------------------------------------------------
from backend import app as workflow

load_dotenv()

# ---------------------------------------------------------
# Logging
# ---------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger("langgraph-fastapi")

# ---------------------------------------------------------
# FastAPI application
# ---------------------------------------------------------
app = FastAPI(
    title="LangGraph Blog Agent",
    description="FastAPI frontend for the existing LangGraph workflow.",
    version="1.0.0",
)