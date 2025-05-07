from custa.renderer.base import ElementRenderer

class ListRenderer(ElementRenderer):
    def render(self, node, render_children):
        content = render_children(node.children)

        list_type = node.props.get("type")
        ordered = node.props.get("ordered") == "true"

        if list_type == "check":
            tag = "ul"
        elif list_type == "definition":
            tag = "dl"
        elif ordered:
            tag = "ol"
        else:
            tag = "ul"

        return f"<{tag} class='custa-list'>{content}</{tag}>"
