from custa.renderer.base import ElementRenderer

class HeadingRenderer(ElementRenderer):
    def render(self, node, render_children):
        text = node.props.get("text", "")
        tag = node.type
        return f"<{tag}>{text}</{tag}>"
