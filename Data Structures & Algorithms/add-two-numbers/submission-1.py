# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #return the sum of the two numbers as a linked list
        #instantly, my thoughts to iterate through the list and take the numbers
        #take 1, then multiply by 10 and add 2, then multiply by 10 and add 
        #same for the seocnd. 
        #then we can make a new linkedList.

        firstNum = 0
        secondNum = 0
        firstPointer = l1
        secondPointer = l2

        while firstPointer:
            firstNum *= 10
            firstNum += firstPointer.val
            firstPointer = firstPointer.next
        
        while secondPointer:
            secondNum *= 10
            secondNum += secondPointer.val
            secondPointer = secondPointer.next
        

        firstStr = str(firstNum)
        secondStr = str(secondNum)
        firstStr = firstStr[::-1]
        secondStr = secondStr[::-1]

        firstNum = int(firstStr)
        secondNum = int(secondStr)
        totalSum = firstNum + secondNum
        strNum = str(totalSum)[::-1]
        head = ListNode(int(strNum[0]))

        listPtr = head
        for i in range(1, len(strNum)):
            listPtr.next = ListNode(int(strNum[i]))
            listPtr = listPtr.next
        return head



        