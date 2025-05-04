from custa.renderer.base import ElementRenderer

class NavFooterRenderer(ElementRenderer):
    def render(self, node, render_children):
        title = node.props.get("title", "")

        content = render_children(node.children)

        print(content)
        
        title_html = f"""
        <div id="nav-header">
            <a id="nav-title" href="https://codepen.io" target="_blank">{title}</a>
            <label for="nav-toggle"><span id="nav-toggle-burger"></span></label>
            <hr />
        </div>
        """ if title else ""
        
        return f'''
        {title_html}

        <div id="nav-content">
            <div class="nav-button"><i class="fas fa-palette"></i><span>Your Work</span></div>
            <div class="nav-button"><i class="fas fa-images"></i><span>Assets</span></div>
            <div class="nav-button"><i class="fas fa-thumbtack"></i><span>Pinned Items</span></div>
            <hr />
            <div class="nav-button"><i class="fas fa-heart"></i><span>Following</span></div>
            <div class="nav-button"><i class="fas fa-chart-line"></i><span>Trending</span></div>
            <div class="nav-button"><i class="fas fa-fire"></i><span>Challenges</span></div>
            <div class="nav-button"><i class="fas fa-magic"></i><span>Spark</span></div>
            <hr />
            <div class="nav-button"><i class="fas fa-gem"></i><span>Codepen Pro</span></div>
            <div id="nav-content-highlight"></div>
        </div>

        <div id="nav-footer">
            <div id="nav-footer-heading">
                <div id="nav-footer-avatar">
                    <img src="https://gravatar.com/avatar/4474ca42d303761c2901fa819c4f2547" />
                </div>

                <div id="nav-footer-titlebox">
                    <div id="nav-footer-title">uahnbu</div>
                    <span id="nav-footer-subtitle">Admin</span>
                </div>

                <button id="logout-button" title="Logout">
                    <i class="fas fa-sign-out-alt"></i>
                </button>
            </div>
        </div>
        '''
