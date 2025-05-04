from custa.parser import Node

def render_text(node: Node) -> str:
    return f"<p>{node.props['text']}</p>"
