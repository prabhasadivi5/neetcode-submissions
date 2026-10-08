class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #given integer array with prices where prices[i] is the price of the coin on ith day
        #may buy and sell with restriction
        #own only one coin at a time
        #as many transactions as we like 
        #return the maximum profit we can achieve

        #we can have the value we are passing down as the totalsum
        #the rows can be the index
        #and the columns can be the coin we have/dont have
        #and then from there we work bottom up
        #dont think we need two arrays
        #dp[i, true] = max [i, False]
        #At any state, all we need to know is if we have a coin, whether we have money, and whether we are on cooldown. 
        #we need to store only three values at a time. 
        #i can do it with a 1d array storing the amount of money we have 
        #do we need to have 3 arrays at each point? 1 is the money with a coin to sell, 1 is with money to hold, and 1 is to buy.
        #we know that hold is i + 2 and also that 


        #what states do we need to store -> i, buy/hold/sell
        #base case: DP[sell], len-1 = 0
        # all we care about is if we have max of a sum with a coin, without a coin, and on hold(always worse than with a coin), but we can keep as with a coin

        withcoin = -1 * prices[0]
        withoutcoin = 0
        maxhold = 0

        for i in range(1, len(prices)):
            newwithoutcoin = max(withoutcoin, maxhold)
            newwithcoin = max(withoutcoin - prices[i], withcoin)
            newmaxhold = max(withcoin + prices[i], maxhold)

            withcoin = newwithcoin
            withoutcoin = newwithoutcoin
            maxhold = newmaxhold
        return max(withcoin, withoutcoin, maxhold)

                             
        

