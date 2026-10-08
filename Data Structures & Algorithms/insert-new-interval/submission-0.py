class Node:
    def __init__(self, left=None, right=None):
        self.nexts = None
        self.prev = None
        self.left = left
        self.right = right


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # build the doubly linked list behind a dummy head
        dummy = Node()
        tail = dummy
        for leftSide, rightSide in intervals:
            node = Node(leftSide, rightSide)
            node.prev = tail          # set prev on the NEW node
            tail.nexts = node
            tail = node

        newLeft, newRight = newInterval

        # find the last node whose start is < newLeft
        currnode = dummy
        while currnode.nexts and currnode.nexts.left < newLeft:
            currnode = currnode.nexts

        # splice the new interval in after currnode
        newNode = Node(newLeft, newRight)
        newNode.prev = currnode
        newNode.nexts = currnode.nexts
        currnode.nexts = newNode
        if newNode.nexts:
            newNode.nexts.prev = newNode

        # merge with the previous node if they overlap
        # (at most one previous node can overlap, since the input is sorted and disjoint)
        p = newNode.prev
        if p is not dummy and p.right >= newNode.left:
            newNode.left = p.left
            newNode.right = max(newNode.right, p.right)
            p.prev.nexts = newNode    # unlink p
            newNode.prev = p.prev

        # keep swallowing following nodes while they overlap
        while newNode.nexts and newNode.nexts.left <= newNode.right:
            newNode.right = max(newNode.right, newNode.nexts.right)
            newNode.nexts = newNode.nexts.nexts
            if newNode.nexts:
                newNode.nexts.prev = newNode

        # convert back to a list
        ret = []
        curr = dummy.nexts
        while curr:
            ret.append([curr.left, curr.right])
            curr = curr.nexts
        return ret