class Solution:
    def climbStairs(self, n: int) -> int:
        #we can use dp for this
        #the number of ways to climb the stairs from a is the number of ways to climb from a + 1 plus a + 1
        #its easier to work bottom down because our base case is climbing from 1 from top is 1 and 2 from top is 2
        #if n == 1, the answer is 1
        #if n == 2, the answer is 2

        #start at n-2, go to zero(exclusive) iterate from -1

        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        twoToTheRight = 1
        oneToTheRight = 2

        for i in range(n-2, 0, -1):
            curr = oneToTheRight + twoToTheRight
            twoToTheRight = oneToTheRight
            oneToTheRight = curr
        
        return oneToTheRight

        