from custa.renderer.base import ElementRenderer


def elevate_inline_props(node, from_tags: set[str]) -> None:
    for child in node.children[:]:
        if child.type in from_tags:
            if "text" in child.props:
                node.props[child.type] = child.props["text"]
                node.children.remove(child)
            elif child.children:
                text_node = child.children[0]
                if text_node.type == "text":
                    node.props[child.type] = text_node.props["text"]
                    node.children.remove(child)



class NavbarRenderer(ElementRenderer):
    def render(self, node, render_children):
        title = node.props.get("text", "")        

        for child in node.children:
            if child.type == "button":
                child.type = "nav_button"
                elevate_inline_props(child, {"icon", "link"})

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
