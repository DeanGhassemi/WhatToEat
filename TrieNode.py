class TrieNode():
    def __init__(self, char='', value: str = ''):
        self._value: str = value
        self._children: ChildrenDictionary = ChildrenDictionary()
        self._char: str = char

    def insert(self, word: str) -> None:

        raise NotImplementedError

    def __contains__(self, key: str):

        raise NotImplementedError

    def __delitem__(self, key: str):

        raise NotImplementedError

    def sort(self, decreasing=False):

        raise NotImplementedError

    def autoComplete(self, prefix, N=10):

        raise NotImplementedError

    def autoCorrect(self, word, errorMax=2):

        raise NotImplementedError

    def merge(self, otherTrie):

        raise NotImplementedError