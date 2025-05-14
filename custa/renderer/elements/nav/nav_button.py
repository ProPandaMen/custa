from custa.renderer.base import ElementRenderer

class NavButtonRenderer(ElementRenderer):
    def render(self, node, render_children):
        text = node.props.get("text", "")
        icon = node.props.get("icon", "")
        link = node.props.get("link", "")

        return f'''
            <a href="{link}" class="nav-button">
                <i data-lucide="{icon}"></i>
                <span>{text}</span>
            </a>
        '''
