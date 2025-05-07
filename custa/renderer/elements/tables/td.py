from custa.renderer.base import ElementRenderer

class TdRenderer(ElementRenderer):
    def render(self, node, render_children):        
        content = render_children(node.children)
        
        return f'''
            <td>{content}</td>
        '''
