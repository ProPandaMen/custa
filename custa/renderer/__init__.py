from typing import List
from custa.parser import Node
from custa.renderer.elements import renderers

def render(nodes: List[Node]) -> str:
    html = []
    
    for node in nodes:
        if node.type == "meta":
            continue

        renderer = renderers.get(node.type)
        
        if renderer:
            html.append(renderer(node))
        else:
            html.append(f"<div class='{node.type}'>{node.props}</div>")
    return "\n".join(html)
