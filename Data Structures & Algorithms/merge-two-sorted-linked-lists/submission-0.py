# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1ptr = list1
        list2ptr = list2
        newhead = ListNode()
        head = newhead

        while list1 or list2:
            if list1 and list2: 
                if list1.val < list2.val:
                    newhead.next = list1
                    newhead = newhead.next
                    list1 = list1.next
                else:
                    newhead.next = list2
                    newhead = newhead.next
                    list2 = list2.next
            elif list1:
                newhead.next = list1
                newhead = newhead.next
                list1 = list1.next
            
            elif list2:
                newhead.next = list2
                newhead = newhead.next
                list2 = list2.next 
        return head.next

        
            