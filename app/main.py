from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pathlib import Path
import json
import os

from app.routes import guest_routes, reservation_routes, table_routes
from app.agents import guest_agent, reservation_agent, table_agent, orchestrator_agent
from app.websocket import table_ws
from app.cli.sync_tools import sync_tools_with_registry

app = FastAPI(
    title="Restaurant AI Agent API",
    description="Multi-agent orchestration with AWS Strands + Bedrock + MCP",
    version="1.0"
)

@app.on_event("startup")
async def startup_event():
    print("🔄 Syncing tool definitions...")
    sync_tools_with_registry()

app.include_router(table_ws.router)


app.include_router(guest_agent.router, prefix="/guest")
app.include_router(reservation_agent.router, prefix="/reservation")
app.include_router(table_agent.router, prefix="/table")
app.include_router(orchestrator_agent.router, prefix="/orchestrator")



@app.get("/tools", tags=["Strands Tools"])
def list_registered_tools():
    """Expose current tool definitions from tool_definitions.json"""
    tool_path = Path("app/tools/tool_definitions.json")
    with open(tool_path) as f:
        tools = json.load(f)
    return JSONResponse(content=tools)
