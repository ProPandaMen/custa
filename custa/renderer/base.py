from custa.parser import Node
from abc import ABC, abstractmethod

class ElementRenderer(ABC):
    def __call__(self, node: Node, render_children) -> str:
        return self.render(node, render_children)

    @abstractmethod
    def render(self, node: Node, render_children) -> str:
        pass
