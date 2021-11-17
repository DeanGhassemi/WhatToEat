from __future__ import annotations
from typing import List, Optional


class Tree:
    """Recursive Tree implementation for balanced meal
        
        === Attributes ===
        root: Optional[str]
        subtrees: List[Tree]

    """
    root: Optional[str]
    subtrees: List[Tree]

    def __init__(self, root: Optional[str], subtrees: List[Tree]):
        self.root = root
        self.subtrees = subtrees

    def isEmpty(self) -> bool:
        """Returns true if the tree is empty

        >>> t = Tree(None, [])
        >>> t.isEmpty()
        True
        """
        return self.root is None

    def __contains__(self, target: str) -> bool:
        """ Check if the tree contains the given string
        
        >>> t = Tree("carbs", [])
        >>> t1 = Tree("breakfast", [t])
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
                
    def insert(self, ingredient: str) -> None:
        """Insert the given string into the tree

        >>> t = Tree("egg", [])
        >>> t1 = Tree("rice", [t])
        >>> t1.insert("bread")
        >>> t1.insert("banana")
        >>> t1.__contains__("bread")
        True
        >>> t1.__contains__("banana")
        """
        if not self.root or self.__contains__(target):
            return None
        # Need library to identify foods as carbs, protein, or fats
            
            

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    '''
    print("Instructions:")
    print("After entering an ingredient, click enter. " +
          "Then enter the next   one")
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