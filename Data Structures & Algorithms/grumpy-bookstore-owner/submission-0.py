class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        #bookstore open for n minutes
        #customers[i] is the net customers?
        # if the owner is grumpy, teh customers entering at that minte are not satisfied
        #need to find the best minutes for the owner to not be grumpy
        #

        #)1)calculate the sum of the customers without grumpy alter
        #)then set all from 0 -> minutes to not grumpy and see the difference
        #)then from there, slide one over, if orignalluy was grumpy, do this otherwise that
        #track max grumpiness, left window, right window

        initialMax = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                initialMax += customers[i]

        currSize = initialMax
        leftWindow = 0
        rightWindow = minutes
        for i in range(rightWindow):
            if grumpy[i] == 1: 
                currSize += customers[i]
        if currSize > initialMax: 
            initialMax = currSize
        
        for i in range(1, len(customers) - rightWindow + 1):
            if grumpy[i-1] == 1:
                currSize -= customers[i-1]
            if grumpy[i+rightWindow-1] == 1:
                currSize += customers[i+rightWindow-1]
            if currSize > initialMax:
                initialMax = currSize
        return initialMax

        