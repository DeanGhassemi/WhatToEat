import math
from TrieNode import TrieNode
from typing import Dict, List, Union

# For help in traversing children
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


class TrieTree:
    def __init__(self, char='', value: str = ''):
        """
        Initializes:
            This node's char, `self._char`, ie. your current character in the
            key
            This node's set of subtrees, 'children', using a dictionary
            This node's value, `self._value`  only set iff its a valid word in
            the dictionary
        """
        self._value = value
        self._children = {}
        self._char = char

    # TASK 1
    def insert(self, word: str) -> None:
        """
        Insert your new word, keep in mind, you must insert all child nodes
        >>> trie = TrieTree()
        >>> trie.insert('apple')
        >>> trie.insert('apples')
        >>> trie.insert('application')
        >>> trie.insert('app')
        >>> trie.insert('about')
        >>> "apple" in str(trie)
        True
        >>> "apples" in str(trie)
        True
        >>> "application" in str(trie)
        True
        >>> "app" in str(trie)
        True
        >>> "about" in str(trie)
        True
        """
        if not word.isalpha():
            return None
        else:
            # Checks if the letter is in the node then moves on to the next node
            for i in range(len(word)):
                if i == len(word) - 1:
                    if word[i] not in self._children:
                        tri = TrieTree(word[i], word)
                        self._children[word[i]] = tri
                    else:
                        self._children[word[i]]._value = word
                    self._children = self.dict_sort(self._children)
                    break
                elif word[i] not in self._children and i + 1 < len(word):
                    tri = TrieTree(word[i])
                    self._children[word[i]] = tri
                    if len(self._children) > 1:
                        self._children = self.dict_sort(self._children)
                self = self._children[word[i]]

    # TASK 2
    def __contains__(self, key: str) -> bool:
        """
        Returns True iff key is in tree, otherwise False
        >>> trie = TrieTree()
        >>> trie.insert("water")
        >>> trie.insert("walter")
        >>> trie.insert("banana")
        >>> trie.insert('ab')
        >>> trie.insert('abs')
        >>> "water" in str(trie)
        True
        >>> "walter" in str(trie)
        True
        >>> "bob" in str(trie)
        False
        >>> "banana" in str(trie)
        True
        >>> "ab" in str(trie)
        True
        >>> "abs" in str(trie)
        True
        """
        if not key.isalpha():
            return False
        else:
            # Checks if the letter is in the node then moves on to the next node
            for i in range(len(key) + 1):
                if i == len(key):
                    if self._value:
                        return True
                elif key[i] in list(self._children.keys()):
                    self = self._children[key[i]]
            return False

    # TASK 3
    def __delitem__(self, key: str) -> None:
        """
        Deletes entry in tree and prunes unecessary branches if key exists,
        otherwise changes nothing
        >>> trie = TrieTree()
        >>> trie.insert("word")
        >>> "word" in trie
        True
        >>> del trie["word"]
        >>> "word" in trie
        False
        >>> str(trie)
        'TrieTree'
        >>> trie.insert('ab')
        >>> trie.insert('abs')
        >>> str(trie)
        'TrieTree\\n   `- a\\n      `- b : ab\\n         `- s : abs'
        >>> del trie['ab']
        >>> str(trie)
        'TrieTree\\n   `- a\\n      `- b\\n         `- s : abs'
        """
        if not self.__contains__(key):
            return None
        else:
            index = 0
            nodes = [self]
            # go down the tree to find the last node and removing the ._value
            while index != len(key):
                if key[index] in list(self._children.keys()):
                    self = self._children[key[index]]
                    nodes.append(self)
                    index += 1
            self._value = ''
            if self._children:  # Cannot remove a node that has children
                return None
            # Going up the tree and cleaning up the nodes/trie
            while index != 0:
                self = nodes[-2]
                index -= 1
                self._children.pop(key[index])
                if len(self._children) >= 1:
                    return None
                nodes.pop(-1)
            return None

    # For sorting the trie
    def dict_sort(self, childrendict: dict) -> dict:
        sorted_keys = sorted(childrendict)
        new = {}
        # Assign key's their proper value
        for key in sorted_keys:
            new[key] = childrendict[key]
        return new

    def preorder_traverse(self) -> List[str]:
        new = []
        for child in self._children:
            if self._children[child]._value:
                new = new + [self._children[child]._value]
            new = new + self._children[child].preorder_traverse()
        return new

    def postorder_traverse(self) -> List[str]:
        words = []
        for i in range(len(self._children) - 1, -1, -1):
            words = words + list(self._children.values())[i]. \
                postorder_traverse()
        if self._value:
            words = words + [self._value]
        return words

    def search(self, word: str, errormax: int, counter: int, prefix: str,
               index: int = -1) -> List[str]:
        words = []
        if not prefix:
            for child in self._children:
                index += 1
                if len(word) > index:
                    if word[index] != child:
                        counter += 1
                elif self._children[child]._value and errormax >= counter:
                    words = words + [self._children[child]._value]
                else:
                    counter += 1
                words = words + \
                        self._children[child].search \
                            (word, errormax, counter, index, prefix)
        else:
            for child in self._children:
                index += 1
                if len(prefix) >= index:
                    self._children[child].search \
                        (word, errormax, counter, index, prefix)
                elif self._children[child]._value and errormax >= counter:
                    words = words + [self._children[child]._value]
                else:
                    counter += 1
                words = words + self._children[child].search \
                    (word, errormax, counter, index)
        return words

    def common_prefix(self, word: str, index=-1) -> str:
        """
        >>> trie = TrieTree()
        >>> trie.insert('app')
        >>> trie.common_prefix('apl')
        'ap'
        """
        prefix = ''
        for child in self._children:
            index = index + 1
            if index >= len(word):
                return prefix
            elif word[index] == child:
                prefix = prefix + child
            prefix = prefix + self._children[child].common_prefix(word, index)
        return prefix

    # TASK 4
    def sort(self, decreasing=False) -> Union[List[str], None]:
        """
        Returns list of words in tree sorted alphabetically
        >>> trie = TrieTree()
        >>> trie.insert('apple')
        >>> trie.insert('apples')
        >>> trie.insert('application')
        >>> trie.insert('app')
        >>> trie.insert('about')
        >>> trie.sort()
        ['about', 'app', 'apple', 'apples', 'application']
        >>> trie.sort(True)
        ['application', 'apples', 'apple', 'app', 'about']
        """
        # I left preorder traversal and postorder traversal outside the method
        # because its more explicit on whats is being done. I wouldn't make
        # sense if i called "sort" in a different method since it implies
        # preorder/postorder traversal
        if decreasing:
            return self.postorder_traverse()
        return self.preorder_traverse()

    # TASK 5
    def autoComplete(self, prefix, N=10):
        """
        if given a valid prefix, return a list containing N number of
        suggestions starting with that prefix in alphabetical order
        else return an empty list
        >>> trie = TrieTree()
        >>> trie.insert('apple')
        >>> trie.insert('dad')
        >>> trie.insert('apples')
        >>> trie.insert('application')
        >>> trie.insert('app')
        >>> trie.insert('about')
        >>> trie.insert('cherry')
        >>> trie.insert('banana')

        >>> trie.autoComplete('a')
        ['about', 'app', 'apple', 'apples', 'application']
        >>> trie.autoComplete('app')
        ['app', 'apple', 'apples', 'application']
        """
        words = self.preorder_traverse()
        words_to_remove = []
        for word in words:
            if prefix not in word[:len(prefix)]:
                words_to_remove = words_to_remove + [word]
        for word in words_to_remove:
            words.remove(word)
        return words[:N]

    # TASK 6
    def autoCorrect(self, word, errorMax=2):
        """
        Given a word, if misspelt return a list of possible valid words from the
        last valid prefix, with up to errorMax errors
        >>> trie = TrieTree()
        >>> trie.insert('dab')
        >>> trie.insert('apple')
        >>> trie.insert('dad')
        >>> trie.insert('dude')
        >>> trie.insert('apples')
        >>> trie.insert('application')
        >>> trie.insert('app')
        >>> trie.insert('about')
        >>> trie.insert("apples")
        >>> trie.insert("application")
        >>> trie.insert('app')
        >>> trie.insert('apple')
        >>> trie.autoCorrect('apl', errorMax=10)
        ['app', 'apple', 'apples', 'application']
        >>> trie.autoCorrect('dea')
        ['dab', 'dad']
        >>> trie.autoCorrect('dod')
        ['dad', 'dude']
        >>> trie.autoCorrect('dea', errorMax=3)
        ['dab', 'dad', 'dude']
        """
        # TODO
        if self.__contains__(word):
            return [word]
        other = TrieTree()
        other.insert(word)
        possible_words = self.search(word, errorMax, 0,
                                     self.common_prefix(word))
        return possible_words

    # TASK 7
    def merge(self, otherTrie: TrieNode):
        """
        Merges another TrieTree into this one
        >>> trie1 = TrieTree()
        >>> trie2 = TrieTree()
        >>> trie1.insert('amazing')
        >>> trie2.insert('amazon')
        >>> trie1.merge(trie2)
        >>> 'amazon' in trie1
        True
        """
        # Find words in both tries
        for word in otherTrie.preorder_traverse():
            if not self.__contains__(word):
                self.insert(word)

    def pPrint(self, _prefix="", _last=True, index=0):
        """
        DONT CHANGE THIS
        """
        ret = ''
        if index:
            ret = _prefix + ("`- " if _last else "|- ") + self._char
            _prefix += "   " if _last else "|  "
            if self._value:
                ret += ' : ' + self._value
            ret += '\n'
        else:
            ret = _prefix + "TrieTree"
            _prefix += "   " if _last else "|  "
            ret += '\n'
        child_count = len(self._children)
        for i, child in enumerate(self._children):
            _last = i == (child_count - 1)
            ret += self._children[child].pPrint(_prefix, _last, index + 1)
        return ret

    def __str__(self):
        return self.pPrint().strip()
    
    
if __name__ == '__main__':
    import doctest

    doctest.testmod()
