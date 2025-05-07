from custa.renderer.base import ElementRenderer

class TbodyRenderer(ElementRenderer):
    def render(self, node, render_children):        
        content_nodes = [child for child in node.children if child.type == "tr"]
        content_html = render_children(content_nodes)
        
        return f'''
            <tbody>
                {content_html}
            </tbody>
        '''
