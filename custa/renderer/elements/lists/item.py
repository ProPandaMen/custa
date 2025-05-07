from custa.renderer.base import ElementRenderer

class ItemRenderer(ElementRenderer):
    def render(self, node, render_children):
        list_type = node.parent.props.get("type") if node.parent else None
        content = render_children(node.children)

        if list_type == "check":
            checked = node.props.get("checked") == "true"
            checkbox = "<input type='checkbox' disabled " + ("checked>" if checked else ">")
            return f"<li>{checkbox} {content}</li>"

        elif list_type == "definition":
            return content

        return f"<li>{content}</li>"
