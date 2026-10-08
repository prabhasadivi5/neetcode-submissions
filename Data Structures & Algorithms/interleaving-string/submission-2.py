class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #return true if s3 is formed by interleaving s1 and s2
        #First bruteforce solution is to use backtracking
        #if it works with each, we can add substring and keep going
        #this is a little slow, so we can use memoization where if we reach a given index with given s and t used up
        #the memo array will be can we reach the end goal given the two interweaved string indexes. So idx[s1], idx[s2] = true or idx[s1], idx s2 = false
        #We can solve the DP problem

        #DP[s1idx][s2idx] = DP[s1idx+1] OR DP[s2idx+1]
        #good to note that some of them are not possible if the next sequence is not there. 
        #now, we know that we only need to store DP[s1idx-1] and DP[s2idx-1]
        # DP[0][0] = DP[0][1] or DP[1][0]
        #track visited as well so we know if its actually false or not
        if len(s3) != len(s1) + len(s2):
            return False
        if len(s1) == 0:
            return s2 == s3
        elif len(s2) == 0:
            return s1 == s3
        visited = set()
        DP = []
        for _ in range(len(s1) + 1):
            row = []
            for _ in range(len(s2) + 1):
                row.append(False)
            DP.append(row)

        s1idx = 0
        s2idx = 0
        DP[len(s1)][len(s2)] = True
        visited.add((len(s1), len(s2)))


        def recurse(s1idx, s2idx):
            print(len(s1), len(s2))
            if (s1idx, s2idx) in visited:
                return DP[s1idx][s2idx]

            if s1idx < len(s1) and s2idx < len(s2) and s3[s1idx+s2idx] == s1[s1idx] and s3[s1idx + s2idx] == s2[s2idx]:
                DP[s1idx][s2idx] = recurse(s1idx + 1, s2idx) or recurse(s1idx, s2idx + 1)
            elif s1idx < len(s1) and s3[s1idx+s2idx] == s1[s1idx]:
                DP[s1idx][s2idx] = recurse(s1idx + 1, s2idx)
            elif s2idx < len(s2) and s3[s1idx+s2idx] == s2[s2idx]:
                DP[s1idx][s2idx] = recurse(s1idx , s2idx + 1)

            visited.add((s1idx, s2idx))
            return DP[s1idx][s2idx]

        recurse(0, 0)
        print(DP)
        return DP[0][0]
        




