import json
import os
import argparse
from pathlib import Path

TOOL_DEF_PATH = Path("app/tools/tool_definitions.json")
MANIFEST_PATH = Path("app/tools/agent_manifest.json")


def validate_tool_definitions():
    print("🔍 Validating tool definitions...")
    with open(TOOL_DEF_PATH) as f:
        tools = json.load(f)

    errors = []
    for tool in tools:
        if "tool_name" not in tool or "endpoint" not in tool:
            errors.append(
                f"Missing keys in tool: {tool.get('tool_name', 'unknown')}")
        if tool.get("method") not in ["GET", "POST"]:
            errors.append(f"Invalid method for tool {tool['tool_name']}")

    if errors:
        print("❌ Validation failed with issues:")
        for err in errors:
            print(f"  - {err}")
        return False
    print("✅ tool_definitions.json is valid.")
    return True


def sync_manifest():
    print("🔁 Syncing agent_manifest.json...")
    with open(TOOL_DEF_PATH) as f:
        tools = json.load(f)

    tool_names = [t["tool_name"] for t in tools]

    manifest = {
        "agent_id": "restaurant-agent-core",
        "tools": tool_names,
        "schemas": "./tool_definitions.json",
        "version": "1.0",
        "author": "RestaurantAI Team",
        "auth": {
            "type": "IAM",
            "role": "restaurant-agent-role"
        }
    }

    with open(MANIFEST_PATH, "w") as f:
        json.dump(manifest, f, indent=2)

    print("✅ agent_manifest.json updated.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Tool definition sync/validate CLI")
    parser.add_argument("--validate", action="store_true",
                        help="Validate tool_definitions.json")
    parser.add_argument("--sync", action="store_true",
                        help="Sync agent_manifest.json from tools")

    args = parser.parse_args()

    if args.validate:
        validate_tool_definitions()
    if args.sync:
        if validate_tool_definitions():
            sync_manifest()
