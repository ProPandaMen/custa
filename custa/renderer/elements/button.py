from custa.renderer.base import ElementRenderer

class ButtonRenderer(ElementRenderer):
    def render(self, node, render_children):
        text = node.props.get("text", "Button")
        link = node.props.get("link", "#")
        return f'<a href="{link}" class="btn">{text}</a>'
