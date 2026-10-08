class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
       #minimum operations to make the words equal. 
       #this is clearly dynamic programming. 
       #there are a few things we need to track.
       #The word we have and the number of operations at any given point
       #can replace up to n characters, delete up to n characters and add up to n characters (as upper bounds)
       #3^n total combinations that we can do
    #    #if we have the word money, and monkeys, if we start from the end, no matter what we either have to replace or delete the s.
    #    #if we delete the s, we have monkey and if we replace we have monkeyy


    #    "m onkeys",
    #    "m oney",
    #     #what if we start from the beginning
    #     #we can either add an m, delete an m, or replace (not needed)
    #     # min money -> money, monkeys -> oney, replace not needed since already an m )

    #     #then the array will look like -> we have to store the index of money are on. And we also ahve to store the index of monkey we are on(if we add a word, still on zero, if we remove add one, if we subtract add one)
    #     #we can then use a dp 

    #     dp(word1, word2) = min(1 + addcase (word1, word2+1), 1 + removecase(word1 + 1, word2), 1 + replace case(word1, word2) -> 
    #     its the same we just use this case without adding one)

    #     #base case is dp = 0 (len(word1), len(word2))
    #     #then dp(word1-1, word2) = 
    #     #fill that whole row, then move upwards. 
    #     #what about the not possible case? if DP(word1) > len(word2), we have to force a remove somewhere. Otherwise, we can do it at the end. 
        dp = [0] * (len(word1) + 1)
        dp[len(word1)] = 0
        prev=dp[::]
        for i in range(len(word2), -1, -1):
            for j in range(len(word1), -1 ,-1):

                if i == len(word2):
                    if j == len(word1):
                        dp[j] = 0
                    else:
                        dp[j] = 1 + dp[j+1]

                elif j == len(word1):
                    dp[j] = 1 + prev[j]
                else:
                    if word2[i] == word1[j]:
                        dp[j] =  + min(1+prev[j], prev[j+1], 1+ dp[j+1])

                    else:
                        dp[j] = 1 + min(prev[j], prev[j+1], dp[j+1])
            prev = dp[:]
        
        return dp[0]

                


        
