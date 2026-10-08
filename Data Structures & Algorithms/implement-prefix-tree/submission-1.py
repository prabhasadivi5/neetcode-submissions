class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = {}
        self.isaword = False


class PrefixTree:

    def __init__(self):
        self.prefixTree = {}

    def insert(self, word: str) -> None:
        currDict = self.prefixTree
        node = None
        for char in word:
            if char not in currDict:          # only create if missing, never overwrite
                currDict[char] = Node(char)
            node = currDict[char]
            currDict = node.next
        node.isaword = True                   # flag the last char's node, not a "" key

    def search(self, word: str) -> bool:
        currDict = self.prefixTree
        node = None
        for char in word:
            if char not in currDict:
                return False
            node = currDict[char]
            currDict = node.next
        return node.isaword

    def startsWith(self, prefix: str) -> bool:
        currDict = self.prefixTree
        for char in prefix:
            if char not in currDict:
                return False
            currDict = currDict[char].next
        return True