from typing import Any, Dict, List

import re

class Node:
    def __init__(self, type_: str, props: Dict[str, Any] = None, children: List["Node"] = None):
        self.type = type_
        self.props = props or {}
        self.children = children or []

    def __repr__(self):
        return f"Node(type={self.type}, props={self.props}, children={self.children})"

def parse_props(text: str) -> Dict[str, str]:
    props = {}
    matches = re.findall(r'(\w+)\s*=\s*"([^"]+)"', text)
    for key, value in matches:
        props[key] = value
    return props

def parse_mks(content: str) -> List[Node]:
    lines = content.splitlines()
    nodes: List[Node] = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if line.startswith("#"):
            key, _, value = line[1:].partition(":")
            nodes.append(Node("meta", {"key": key.strip(), "value": value.strip()}))
        elif line.startswith("@"):  # tag
            match = re.match(r"@(\w+)(\((.*?)\))?", line)
            if match:
                tag = match.group(1)
                props_text = match.group(3) or ""
                props = parse_props(props_text)
                nodes.append(Node(tag, props))
            else:
                raise ValueError(f"Invalid tag syntax: {line}")
        else:
            nodes.append(Node("text", {"text": line}))

    return nodes
