from custa.renderer.base import ElementRenderer

class TheadRenderer(ElementRenderer):
    def render(self, node, render_children):
        content_nodes = [child for child in node.children if child.type == "tr"]

        content_html = render_children(content_nodes)
        
        return f'''
            <thead>
                {content_html}
            </thead>
        '''
