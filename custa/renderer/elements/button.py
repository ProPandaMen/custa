from custa.parser import Node

def render_button(node: Node) -> str:
    text = node.props.get("text", "Button")
    link = node.props.get("link", "#")
    return f'<a href="{link}" class="btn">{text}</a>'
