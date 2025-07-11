from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pathlib import Path
from app.cli.sync_tools import sync_tool_registry
import json


from app.routes import guest_routes, reservation_routes, table_routes


from app.agents import guest_agent, reservation_agent, table_agent


from app.websocket import table_ws

app = FastAPI(
    title="Restaurant AI Agent API",
    description="Multi-agent orchestration with AWS Strands + Bedrock + MCP",
    version="1.0.0"
)

app.include_router(table_ws.router)


app.include_router(guest_routes.router, prefix="/guest", tags=["Guest"])
app.include_router(reservation_routes.router,
                   prefix="/reservation", tags=["Reservation"])
app.include_router(table_routes.router, prefix="/table", tags=["Table"])


app.include_router(guest_agent.router, prefix="/guest")
app.include_router(reservation_agent.router, prefix="/reservation")
app.include_router(table_agent.router, prefix="/table")


@app.get("/tools", tags=["Strands Tools"])
def list_registered_tools():
    """Expose tool definitions as expected by AWS Strands SDK and MCP"""
    path = Path("app/tools/tool_definitions.json")
    if not path.exists():
        return JSONResponse(content={"error": "tool_definitions.json not found"}, status_code=404)

    with open(path) as f:
        tools = json.load(f)
    return JSONResponse(content=tools)


@app.on_event("startup")
async def auto_sync_tools():
    print("🔁 Syncing tools to registry...")
    sync_tool_registry(sync=True)
