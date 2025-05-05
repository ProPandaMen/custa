from custa.renderer.base import ElementRenderer

class NavFooterRenderer(ElementRenderer):
    def render(self, node, render_children):
        return f'''
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
