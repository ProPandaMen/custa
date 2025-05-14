from custa.renderer.base import ElementRenderer

class NavbarRenderer(ElementRenderer):
    def render(self, node, render_children):
        title = node.props.get("title", "")

        footer_nodes = [child for child in node.children if child.type == "nav_footer"]
        content_nodes = [child for child in node.children if child.type != "nav_footer"]

        content_html = render_children(content_nodes)
        footer_html = render_children(footer_nodes)
        
        return f'''
            <div id="nav-header">
                <img src="static/logo.svg" alt="Logo"/>
                <a id="nav-title" href="/" target="_blank">{title}</a>
                <label for="nav-toggle"><span id="nav-toggle-burger"></span></label>
            </div>

            <div id="nav-content">
                <hr />
                {content_html}
                <div id="nav-content-highlight"></div>
            </div>

            {footer_html}
        '''
