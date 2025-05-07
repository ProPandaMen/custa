from custa.renderer.base import ElementRenderer

class ThRenderer(ElementRenderer):
    def render(self, node, render_children):        
        content = render_children(node.children)
        
        return f'''
            <th>{content}</th>
        '''
