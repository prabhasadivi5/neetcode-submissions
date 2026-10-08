from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #2D grid, each cell has 0 for empty, 1 for fressh, and 2 for rotten
        #every minute, if next to a rotten fruit, then the fresh fruit rots as well 
        #minimum number of minutes that elapse until zero fresh fruits remain 
        #Since its number of minutes and it spreads, we are using a bfs
        #Since multiple, we iterate through, do a bfs starting with the multiple and keep going
        #Now, we need to worry about the edge case -> since its returning -1 if not all fruits rotten -> we can count number of ripe fruits at the beginning, and if rotten = ripe by the end, then we are good 
        myq = deque()
        bananas = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                print(grid[i][j])
                if grid[i][j] == 2:
                    myq.append((i,j))
                    bananas += 1
                elif grid[i][j] == 1:
                    bananas += 1
        if bananas == 0:
            return  0 
        #run the bfs, count the number of iterations, end when the queue is empty, if fresh != 0, then we have an issue
        iterations = -1
        while myq:
            for i in range(len(myq)):
                bananas -= 1
                ival, jval = myq.popleft()
                if ival < len(grid) - 1 and grid[ival + 1][jval] == 1:
                    myq.append((ival +1, jval))
                    grid[ival + 1][jval] = 2
                if ival > 0 and grid[ival-1][jval] == 1:
                    myq.append((ival-1, jval))
                    grid[ival-1][jval] = 2
                if jval > 0 and grid[ival][jval -1] == 1:
                    myq.append((ival, jval - 1))
                    grid[ival][jval-1] = 2
                if jval < len(grid[0]) - 1 and grid[ival][jval + 1] == 1:
                    myq.append((ival, jval + 1))
                    grid[ival][jval + 1] = 2
            iterations += 1
        if(bananas != 0):
            return -1 
        return iterations

            
            

        

        




        