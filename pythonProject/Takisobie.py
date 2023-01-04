from typing import Any, List, Callable, Union

class TreeNode:
    value: Any
    children: List['TreeNode']
    def __init__(self, value: Any):
        # Przechowuje wartość węzła
        self.value = value
        # Przechowuje listę dzieci węzła
        self.children = []

    def is_leaf(self) -> bool:
        # Zwraca True, jeśli węzeł nie ma dzieci, w przeciwnym razie False
        return not self.children

    def add(self, child: 'TreeNode') -> None:
        # Dodaje węzeł przekazany w argumencie jako dziecko
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        # Odwiedź bieżący węzeł i wykonaj funkcję visit na nim
        visit(self)
        # Dla wszystkich dzieci bieżącego węzła wywołaj metodę for_each_deep_first()
        for child in self.children:
            child.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        # Tworzy pustą kolejkę FIFO i dodaje do niej bieżący węzeł
        queue = [self]
        # Dopóki kolejka nie jest pusta:
        while queue:
            # Pobierz pierwszy element z kolejki
            node = queue.pop(0)
            # Odwiedź węzeł i wykonaj funkcję visit na nim
            visit(node)
            # Dodaj wszystkie dzieci węzła do kolejki
            queue.extend(node.children)

    def search(self, value: Any) -> Union['TreeNode', None]:
        # Jeśli wartość bieżącego węzła jest równa szukanej wartości, zwraca bieżący węzeł
        if self.value == value:
            return self

        # Dla wszystkich dzieci bieżącego węzła wywołaj metodę search()
        for child in self.children:
            result = child.search(value)
            # Jeśli metoda zwróciła węzeł, zwróć go
            if result:
                return result

        # Jeśli nie znaleziono węzła z szukaną wartością, zwróć None
        return None

    def __str__(self) -> str:
        # Zwraca wartość węzła jako napis
        return str(self.value)


