from custa.renderer.base import ElementRenderer

class TrRenderer(ElementRenderer):
    def render(self, node, render_children):
        content_nodes = [child for child in node.children if child.type in ["td", "th"]]
        content_html = render_children(content_nodes)
        
        return f'''
            <tr>
                {content_html}
            </tr>
        '''
