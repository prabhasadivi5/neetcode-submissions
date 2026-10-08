class Node:
    def __init__(self, key: int, val: int, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.oldest = None
        self.newest = None
        self.mydict = {}

    def get(self, key: int) -> int:
        if key not in self.mydict:
            return -1

        currNode = self.mydict[key]

        # Already newest
        if currNode is self.newest:
            return currNode.val

        # Remove currNode from its current position
        if currNode.left:
            currNode.left.right = currNode.right
        else:
            self.oldest = currNode.right

        if currNode.right:
            currNode.right.left = currNode.left
        else:
            self.newest = currNode.left

        # Put currNode at newest
        currNode.left = self.newest
        currNode.right = None
        self.newest.right = currNode
        self.newest = currNode

        return currNode.val

    def put(self, key: int, value: int) -> None:

        # Key already exists
        if key in self.mydict:
            currNode = self.mydict[key]
            currNode.val = value

            # Move to newest
            if currNode is not self.newest:

                if currNode.left:
                    currNode.left.right = currNode.right
                else:
                    self.oldest = currNode.right

                if currNode.right:
                    currNode.right.left = currNode.left
                else:
                    self.newest = currNode.left

                currNode.left = self.newest
                currNode.right = None
                self.newest.right = currNode
                self.newest = currNode

            return

        # New key
        newNode = Node(key, value)
        self.size += 1

        # First node
        if self.size == 1:
            self.oldest = newNode
            self.newest = newNode
            self.mydict[key] = newNode
            return

        # Add to newest
        newNode.left = self.newest
        self.newest.right = newNode
        self.newest = newNode
        self.mydict[key] = newNode

        # Evict oldest
        if self.size > self.capacity:
            oldNode = self.oldest
            del self.mydict[oldNode.key]

            self.oldest = oldNode.right
            self.oldest.left = None

            self.size -= 1