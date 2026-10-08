class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        



        usedset = set()
        #1)iterate through every node in the graph
        #2)start a dfs starting at every node and index to zero
        #3)if the node is not equal to the letter at the index, return false
        #4)if the node is equal to the value, add it to the usedarr, and run dfs on it at the next idx
        #5)then do dfs on the rest of the neighbors
        #6)return true if any of the functions return true (right after)
        #in between neighbors, make sure to pop from the array in the dfs
        def dfs(x, y, idx):
            if (x,y) in usedset:
                return False
            if board[x][y] != word[idx]:
                return False
            
            if board[x][y] == word[idx] and idx == len(word) - 1:
                return True 

            usedset.add((x,y))
            retTrue = False 
            if x > 0 and (x-1, y) not in usedset:
                retTrue = dfs(x-1, y, idx + 1)
                if retTrue:
                    return True
            if x < len(board) -1  and (x+1, y) not in usedset:
                retTrue = dfs(x+1, y, idx + 1)
                if retTrue:
                    return True
            if y > 0 and (x, y - 1) not in usedset:
                retTrue = dfs(x, y - 1, idx + 1)
                if retTrue:
                    return True
            if y < len(board[0]) - 1 and (x, y + 1) not in usedset:
                retTrue = dfs(x, y+1, idx + 1)
                if retTrue:
                    return True
            usedset.remove((x,y))
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        
        return False

                


        