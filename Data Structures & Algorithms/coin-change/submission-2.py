class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:



        #This is a dynamic programming 
        #first we identify what each state to be
        #then, the decisions at each state 
        #think if the dp replies on the whole table or just the last two rows
        #Then base cases 
        #Then, we can choose the order
        #

        #say we want to identify each state as the amount of money
        #at each state, we need to track the amount of coins and the minimum money to get there 
        #the base case is to get 0, we need 0. Additionally, to get any value in coins, we need 1
        #2 ways to do this. Start from all of the base cases and use memoization to track how far away we are from the end. This is a little more. We iterate it, dp[a] = min(dp[a], 1 + dp[a-c])
        #we can also build top down -> dp[a] = min(dp[a], dp[a-c])
        #then keep the base cases. 
        #we need to track the 1d array first, and then i can optimize to only count dp[a-c]
        dpArr = [9999999] * (amount + 1)
        def dp(currSum):

            #if the coin does not reach zero, we want it to not work 
            if currSum < 0:
                return -1 
            #working base case 
            if currSum == 0:
                return 0
            #if we already know it doesnt work, we dont waste time 
            if dpArr[currSum] == -1:
                return -1

            #if we already have it, we dont waste time
            if dpArr[currSum] < 9999999:
                return dpArr[currSum]
            else:
            #the issue, is if we have -1, then the min will be less 
                for coin in coins:
                    currCoinVal = 1 + dp(currSum-coin)
                    if currCoinVal == 0:
                        currCoinVal = 9999999
                    dpArr[currSum] = min(dpArr[currSum], currCoinVal)
                if dpArr[currSum] == 9999999:
                    dpArr[currSum] = -1 
            return dpArr[currSum]

        temp = dp(amount)
        return temp