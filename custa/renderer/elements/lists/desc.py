from custa.renderer.base import ElementRenderer

class DescRenderer(ElementRenderer):
    def render(self, node, render_children):
        return f"<dd>{render_children(node.children)}</dd>"
