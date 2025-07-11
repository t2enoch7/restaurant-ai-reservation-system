import json
import os
import argparse
from pathlib import Path
from app.agents import guest_agent, reservation_agent, table_agent

TOOL_DEF_PATH = Path("app/tools/tool_definitions.json")
MANIFEST_PATH = Path("app/tools/agent_manifest.json")


def validate_tool_definitions():
    print("🔍 Validating tool_definitions.json...")
    if not TOOL_DEF_PATH.exists():
        print("❌ tool_definitions.json not found.")
        return False

    with open(TOOL_DEF_PATH) as f:
        tools = json.load(f)

    errors = []
    for tool in tools:
        if "tool_name" not in tool or "endpoint" not in tool:
            errors.append(f"Missing required fields in tool: {tool}")
        if tool.get("method") not in ["GET", "POST"]:
            errors.append(f"Invalid HTTP method for {tool.get('tool_name')}")

    if errors:
        print("❌ Found issues in tool definitions:")
        for e in errors:
            print(f"  - {e}")
        return False

    print("✅ tool_definitions.json is valid.")
    return True


def sync_manifest_from_agents():
    print("🔁 Syncing agent_manifest.json from registered agents...")

    # Aggregate all agents
    agents = [guest_agent, reservation_agent, table_agent]

    tool_names = []
    for agent in agents:
        for tool in agent.tools:
            tool_names.append(tool.name)

    manifest = {
        "agent_id": "restaurant-orchestrator",
        "tools": tool_names,
        "schemas": str(TOOL_DEF_PATH),
        "version": "1.0",
        "author": "RestaurantAI Team",
        "auth": {
            "type": "IAM",
            "role": "restaurant-agent-role"
        }
    }

    with open(MANIFEST_PATH, "w") as f:
        json.dump(manifest, f, indent=2)

    print("✅ agent_manifest.json written.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Validate and sync tool definitions and agent manifest"
    )
    parser.add_argument("--validate", action="store_true",
                        help="Validate tool definitions")
    parser.add_argument("--sync", action="store_true",
                        help="Sync manifest from active agents")

    args = parser.parse_args()

    if args.validate:
        validate_tool_definitions()
    if args.sync:
        if validate_tool_definitions():
            sync_manifest_from_agents()
