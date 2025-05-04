from custa.parser import Node

def render_heading(node: Node) -> str:
    text = node.props.get("text", "")
    return f"<{node.type}>{text}</{node.type}>"
