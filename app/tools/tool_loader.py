import json
from pathlib import Path
from strands_sdk import Tool


def load_tools(path: str) -> list:
    tool_path = Path(path)
    with open(tool_path) as f:
        tool_defs = json.load(f)

    return [Tool.from_dict(tool) for tool in tool_defs]
