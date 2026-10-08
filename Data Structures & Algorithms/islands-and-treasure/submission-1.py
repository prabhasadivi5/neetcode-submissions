from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #we are given a grid initialized with a water cell that cannot be traversed, a treasure chest, and a land cell that can be traversed 
        #each land cell with a distance to each treasure chest
        #instantly a breadth first search comes because we want to count hte number of steps, and we only have to do the breadth expansion once (visit each once) instead of doing a dfs and dfs will be more complicated because we have to track visited
        #since theres multiple starting points, we can just do a bfs from all of the trasure chests
        #can use a set to track visited, count treasure chests as alr visited since no repeat want 
        #Algo is simple: have a visited set, add chests to set, add chests to queue, as we traverse each time length of queue(breadth first search), add unvisited to set, and once set size = grid size, we can finish.
        myq = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    myq.append((i,j))
        
        dist = 1
        while len(myq) > 0:
            for _ in range(len(myq)):
                val = myq.popleft()
                i = val[0]
                j = val[1]
                if i + 1 < len(grid) and grid[i+1][j] >= 2147483:
                    myq.append((i+1, j))
                    grid[i+1][j] = dist
                if i - 1 >= 0 and  grid[i-1][j] >2147483: 
                    myq.append((i-1, j))
                    grid[i-1][j] = dist
                if j -1 >=0 and grid[i][j-1] >2147483: 
                    myq.append((i, j - 1))
                    grid[i][j-1] = dist
                if j + 1 < len(grid[0]) and grid[i][j+1] >2147483: 
                    myq.append((i, j + 1))
                    grid[i][j+1] = dist
            dist += 1
                

                

        