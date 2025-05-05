from custa.renderer.base import ElementRenderer

class NavButtonRenderer(ElementRenderer):
    def render(self, node, render_children):
        text = node.props.get("text", "")
        icon = node.props.get("icon", "")

        return f'''
            <div class="nav-button">
                <i class="{icon}"></i>
                <span>{text}</span>
            </div>
        '''
