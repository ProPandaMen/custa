from custa.renderer.base import ElementRenderer

class HrRenderer(ElementRenderer):
    def render(self, node, render_children):
        return "<hr />"
