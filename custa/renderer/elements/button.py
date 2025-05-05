from custa.renderer.base import ElementRenderer

class ButtonRenderer(ElementRenderer):
    def render(self, node, render_children):
        text = node.props.get("text", "Button")
        link = node.props.get("link", "#")

        color = node.props.get("color", "primary")

        return f'<a class="button {color}" href="{link}" class="btn">{text}</a>'
