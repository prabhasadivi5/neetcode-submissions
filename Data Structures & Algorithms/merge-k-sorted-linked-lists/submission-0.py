import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #k sorted linked lists. we have a list of lists. 
        #so for k sorted, we have the top from each list. 
        #we add the top of the heap to the linkedlist
        #then from that list if there is a node, we move to the next ptr of that node. 
        #why cant we put the head of each node into the heap, -> no idea how to sort nodes or if functionality even exists for that 
        #one solution is to keep a dictionary of all the linkedlists. Then, keep track of the index. 
        #push a tuple to the heap storing the node top value and the index. 
        #if the top value is one Node, just add to the list and do nothing (dont add to the heap again)
        #otherwise, add the value from the new node into the heap and then add . 
        

        #make the dictionary and the default heap 
        minheap = []
        nodesDict = {}
        for i, linkedlist in enumerate(lists):
            if lists[i]:
                nodesDict[i] = lists[i]
                minheap.append((lists[i].val, i))

        heapq.heapify(minheap)
        head = ListNode()
        currnode = head
        #now do the heap algorithm
        #pop from heap, add that node to the return list
        #then go to next node inside the dict, if it is not none, heapq.heappush
        #keep doing this while heap exists

        while minheap: 
            topval, topIdx = heapq.heappop(minheap)
            topNode = nodesDict[topIdx]

            currnode.next = topNode 
            currnode = currnode.next
            nodesDict[topIdx] = topNode.next
            if topNode.next:
                heapq.heappush(minheap, (topNode.next.val, topIdx))
                
        return head.next


        





