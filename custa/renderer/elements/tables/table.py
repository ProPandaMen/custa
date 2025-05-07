from custa.renderer.base import ElementRenderer

class TableRenderer(ElementRenderer):
    def render(self, node, render_children):        
        footer_nodes = [child for child in node.children if child.type == "thead"]
        content_nodes = [child for child in node.children if child.type == "tbody"]

        thead_html = render_children(content_nodes)
        tbody_html = render_children(footer_nodes)
        
        return f'''
            <div class="table-container">
                <table class="custa-table">
                    {thead_html}
                    {tbody_html}
                </table>

                <div class="pagination">
                    <button class="page-btn active">1</button>
                    <button class="page-btn">2</button>
                    <button class="page-btn">3</button>
                    <span class="dots">…</span>
                    <button class="page-btn">10</button>
                </div>
            </div>
        '''
