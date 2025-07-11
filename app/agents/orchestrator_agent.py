from strands_sdk import Agent

from app.tools.tool_loader import load_tools

MAIN_SYSTEM_PROMPT = """
You are the Restaurant Orchestrator Agent. Your job is to coordinate restaurant operations by:
- Checking table availability
- Creating reservations
- Retrieving guest preferences
- Updating table statuses

Always respond using available tools. You do not guess — instead, invoke the appropriate tool with correct parameters.
"""

tools = load_tools("app/tools/tool_definitions.json")


orchestrator_agent = Agent(
    name="OrchestratorAgent",
    system_prompt=MAIN_SYSTEM_PROMPT,
    tools=tools
)
