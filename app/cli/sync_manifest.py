import json
import os
from pathlib import Path

TOOL_DEFINITION_PATH = Path("app/tools/tool_definitions.json")
MANIFEST_OUTPUT_PATH = Path("app/tools/agent_manifest.json")


def validate_tool(tool: dict) -> bool:
    required_fields = {"tool_name", "description", "input_schema",
                       "output_schema", "endpoint", "method", "auth"}
    missing = required_fields - tool.keys()
    if missing:
        print(f"❌ Tool {tool.get('tool_name')} missing fields: {missing}")
        return False
    return True


def generate_manifest():
    with open(TOOL_DEFINITION_PATH) as f:
        tools = json.load(f)

    valid_tools = [t for t in tools if validate_tool(t)]

    manifest = {
        "agent_name": "RestaurantAgentSystem",
        "tools": valid_tools,
        "version": "1.0"
    }

    with open(MANIFEST_OUTPUT_PATH, "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"✅ agent_manifest.json generated with {len(valid_tools)} tools")


if __name__ == "__main__":
    generate_manifest()
