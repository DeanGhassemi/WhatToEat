from __future__ import annotations
from typing import List


class Tree:
    """Recursive Tree implementation for balanced meal
        
        === Attributes ===
        root: Optional[str]
        subtrees: List[Tree]

    """
    root: str
    subtrees: List[Tree]

    def __init__(self, root: Optional[str], subtrees: List[Tree]):
        self.root = root
        self.subtrees = subtrees

    def __contains__(self, target: str) -> bool:
        """
        Check if the tree contains the given string
        >>> t = Tree("egg", [])
        >>> t1 = Tree("rice", [t])
        >>> t1.__contains__("rice")
        True
        >>> t1.__contains__("egg")
        True
        """
        if self.root is None:
            return False
        elif self.root == target:
            return True
        else:
            for subtree in self.subtrees:
                if subtree.__contains__(target):
                    return True
            return False
                
    # def insert(self, ingredient: str) -> None:


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    '''
    print("Instructions:")
    print("After entering an ingredient, click enter. " +
          "Then enter the next one")
    print("When you are done, please type finished")
    print("What ingredients do you have?")
    ingredients = []
    finished = False
    while not finished:
        food = input("")
        if food == "finished":
            finished = True
        else:
            ingredients.append(food.strip())
'''