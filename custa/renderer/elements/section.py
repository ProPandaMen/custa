from custa.renderer.base import ElementRenderer

class SectionRenderer(ElementRenderer):
    def render(self, node, render_children):
        content = render_children(node.children)
        return f"<section>{content}</section>"
