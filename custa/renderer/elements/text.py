from custa.renderer.base import ElementRenderer

class TextRenderer(ElementRenderer):
    def render(self, node, render_children):
        text = node.props.get("text", "").strip()
        return f"<p>{text}</p>" if text else ""
