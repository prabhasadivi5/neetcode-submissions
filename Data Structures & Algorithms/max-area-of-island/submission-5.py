from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #maximum area of an island
        #Island is group of zeros or 1s connected horizontally or vertically
        #we iterate through the entire grid
        #we first check if this is already part of an island we visited
        #if not, we start the island search and track length using bfs or dfs. 
    #check next grid spot and keep going 
    #ill use a bfs because its simpler 


    #set up the visited set, and max count
        visited = set()
        biggestIsland = 0

    #iterate through the islands
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #first check if we already added, then do the BFS/DFS
                if (i,j) in visited or grid[i][j] == 0:
                    continue

                #we will do BFS with a queue
                myq = deque()
                myq.append((i,j))
                currSize = 0
                val = grid[i][j]
                visited.add((i,j))
                while len(myq) > 0:
                    currSize += 1
                    currx, curry = myq.pop()
                  
                    
                
                #now time for the conditionals. Check if valid grid spot, if not in visited, and if the new val equals to the val we calculated. there are 4 nighbors that we can count
                    if(currx < len(grid) - 1 and (currx+1, curry) not in visited and grid[currx+1][curry] == val):
                        myq.append((currx + 1, curry))
                        visited.add((currx+1,curry))

                    if(currx > 0  and (currx - 1, curry) not in visited and grid[currx-1][curry] == val):
                        myq.append((currx - 1, curry))
                        visited.add((currx-1,curry))

                    if(curry < len(grid[0]) - 1 and (currx, curry + 1) not in visited and grid[currx][curry+1] == val):
                        myq.append((currx , curry + 1))
                        visited.add((currx,curry+1))
                    
                    if(curry > 0 and (currx, curry - 1) not in visited and grid[currx][curry-1] == val):
                        myq.append((currx , curry - 1))
                        visited.add((currx,curry-1))
                biggestIsland = max(biggestIsland, currSize)
        return biggestIsland
                
                    

                    
                


            
                
                
        