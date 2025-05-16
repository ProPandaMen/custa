from typing import Any, Dict, List, Tuple

import re


class Node:
    def __init__(self, type_: str, props: Dict[str, Any] = None, children: List["Node"] = None):
        self.type = type_
        self.props = props or {}
        self.children = children or []

    def __repr__(self):
        return f"Node(type={self.type}, props={self.props}, children={self.children})"


def get_indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def parse_props(text: str) -> Dict[str, str]:
    return dict(re.findall(r'(\\w+)\\s*=\\s*"([^"]+)"', text))


def parse_tag_line(line: str) -> Tuple[str, Dict[str, str]]:
    match = re.match(r":(\w+)(\((.*?)\))?(?:\s+(.*))?", line)
    if not match:
        raise ValueError(f"Invalid tag syntax: {line}")
    
    tag = match.group(1)
    props_text = match.group(3)
    inline_text = match.group(4)

    props = parse_props(props_text or "")
    if props_text is None and inline_text:
        props["text"] = inline_text

    return tag, props


def extract_inline_props_from_children(children: List[Node]) -> Tuple[Dict[str, str], List[Node]]:
    props = {}
    remaining_children = []
    for child in children:
        if isinstance(child, Node) and len(child.children) == 1 and child.children[0].type == "text":
            props[child.type] = child.children[0].props["text"]
        else:
            remaining_children.append(child)
    return props, remaining_children


def parse_block(lines: List[str], start: int, base_indent: int) -> Tuple[List[Node], int]:
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

        if line.startswith(":"):
            tag, props = parse_tag_line(line)

            next_indent = get_indent(lines[i+1]) if i+1 < len(lines) else 0
            if next_indent > indent:
                children, consumed = parse_block(lines, i+1, next_indent)
                if not props:
                    extracted, children = extract_inline_props_from_children(children)
                    props.update(extracted)
                nodes.append(Node(tag, props, children))
                i = consumed - 1
            else:
                nodes.append(Node(tag, props))
        else:
            nodes.append(Node("text", {"text": line}))
        i += 1

    return nodes, i


def parse_mks(content: str) -> List[Node]:
    lines = content.splitlines()
    root_nodes, _ = parse_block(lines, 0, 0)
    
    return root_nodes
