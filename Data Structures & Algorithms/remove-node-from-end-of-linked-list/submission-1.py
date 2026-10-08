# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #get to the end, count the number of nodes, then start over, count steps, track one after the next save that, and then skip it
        tracker = head
        size = 0
        while tracker:
            size += 1
            tracker = tracker.next
        

        #now find distance from beginning. Two from the end is one from the last one. need to travel n-2 from the starting node because start at one
        dist = size - n
        #edge cases: last node and first node. 
        if dist == 0: 
            return head.next

        #now remove
        curr = head
        for i in range(dist - 1):
            curr = curr.next
        
        if n == 1:
            curr.next = None
            return head
        
        curr.next = curr.next.next
        return head




        