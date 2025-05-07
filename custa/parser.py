from typing import Any, Dict, List, Tuple

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

    def get_indent(line: str) -> int:
        return len(line) - len(line.lstrip(" "))

    def parse_block(start: int, base_indent: int) -> Tuple[List[Node], int]:
        nodes: List[Node] = []
        i = start
        while i < len(lines):
            raw_line = lines[i]
            if not raw_line.strip():
                i += 1
                continue

            indent = get_indent(raw_line)
            if indent < base_indent:
                break
            line = raw_line.strip()

            if line.startswith("#"):
                key, _, value = line[1:].partition(":")
                nodes.append(Node("meta", {"key": key.strip(), "value": value.strip()}))
            elif line.startswith("@"):
                match = re.match(r"@(\w+)(\((.*?)\))?(?:\s+(.*))?", line)

                if match:
                    tag = match.group(1)
                    props = parse_props(match.group(3) or "")
                    text_content = match.group(4)

                    children = []
                    if text_content:
                        children = [Node("text", {"text": text_content})]

                    next_indent = get_indent(lines[i+1]) if i+1 < len(lines) else 0
                    if next_indent > indent:
                        block_children, consumed = parse_block(i+1, next_indent)
                        parent_node = Node(tag, props, block_children)
                        for child in block_children:
                            child.parent = parent_node
                        nodes.append(parent_node)
                        i = consumed - 1
                    else:
                        parent_node = Node(tag, props, children)
                        for child in children:
                            child.parent = parent_node
                        nodes.append(parent_node)
                else:
                    raise ValueError(f"Invalid tag syntax: {line}")
            else:
                nodes.append(Node("text", {"text": line}))
            i += 1
        return nodes, i

    root_nodes, _ = parse_block(0, 0)
    return root_nodes
