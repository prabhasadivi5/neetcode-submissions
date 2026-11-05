class Solution:
    def numSquares(self, n: int) -> int:
        #so first idea is to take all the perfect squares less than that number so if 13, we have 1, 2, 3
        #There has to be a math trick here on how perfect squres add up. 
        #We have the option to also use 1 multiple times. 
        #we can start at the biggest perfect square and make our way down to 1. 
        #will it always be optimal to use a bigger number over a smaller number 

        #60
        #maybe we can do dynamic programming where we take every sum up to a value
        #so we know we have our numbers bank and our sum. This is basically coin change 
        #We can iterate from 0 to whatever and say o(n) = min (o -> n - all). 
        #the runtime for this is the number(n) times the number of perfect squares before it(o(n))
        #we can use storage as o(m) but for storage purposes, we are good

        squareNumbers = []
        i = 1
        while i*i <= n:
            squareNumbers.append(i*i)
            i += 1
        

        mindists = [n+1] * (n + 1)
        mindists[0] = 0
        for i in range(1, n + 1):
            mintime = n + 1
            for val in squareNumbers:
                if i - val < 0:
                    continue
                if mindists[i-val] < mintime:
                    mintime = 1 + mindists[i-val]
            mindists[i] = mintime
        return mindists[n]
