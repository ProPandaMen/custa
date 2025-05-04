from custa.renderer.base import ElementRenderer

class NavButtonRenderer(ElementRenderer):
    def render(self, node, render_children):
        
        return f'''
            <div class="nav-button">
                <i class="fas fa-palette"></i>
                <span>Your Work</span>
            </div>
        '''
