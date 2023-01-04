from typing import Any, List, Callable, Union
import graphviz

class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value: Any) -> None:
        self.value = value
        self.children = []

    """
    Sprawdza czy węzeł nie ma dzieci. Zwraca True, jeśli węzeł jest liściem, w przeciwnym razie False.
    """

    def is_leaf(self) -> bool:
        return not self.children

    """
    Dodaje węzeł przekazany w argumencie jako dziecko.
    """
    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    """
    Przechodzi po węzłach metodą deep first i dla każdego węzła wywołuje funkcję visit.
    """

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)

        for child in self.children:
            child.for_each_deep_first(visit)

    """
    Przechodzi po węzłach metodą level order i dla każdego węzła wywołuje funkcję visit.
    """

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        queue = [self]

        while queue:
            node = queue.pop(0)
            visit(node)
            queue.extend(node.children)

    """
    Sprawdza czy bieżący węzeł lub jego dzieci zawierają wartość podaną w parametrze, przy użyciu dowolnej metody przechodzenia po węzłach.
    """

    def search(self, value: Any) -> Union['TreeNode', None]:
        if self.value == value:
            return self

        for child in self.children:
            result = child.search(value)
            if result:
                return result

        return None

    def __str__(self) -> str:
         # Zwraca wartość węzła jako napis
        return str(self.value)

def save_tree_as_png(root: TreeNode, filename: str) -> None:
    def add_nodes_and_edges(graph, node):
        for child in node.children:
            graph.edge(str(node.value), str(child.value))
            add_nodes_and_edges(graph, child)

    graph = graphviz.Digraph()
    add_nodes_and_edges(graph, root)
    graph.render(filename, format="png")

root = TreeNode(0)
child1 = TreeNode(1)
child2 = TreeNode(2)
root.add(child1)
root.add(child2)
child1.add(TreeNode(3))
child1.add(TreeNode(4))
child2.add(TreeNode(5))
save_tree_as_png(root, "tree.png")


