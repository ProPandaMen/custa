from custa.renderer.base import ElementRenderer

class TermRenderer(ElementRenderer):
    def render(self, node, render_children):
        return f"<dt>{render_children(node.children)}</dt>"
