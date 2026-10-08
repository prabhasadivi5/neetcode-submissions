class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #each row has 1-9 without duplicates
        #each column has 1-9 without duplicates
        #each box must contain 1-9 without duplicates
        #does not need to be solvable
        #first intuition is to go through rows (o m*n) then columns o(m*n) then grids o(m*n)
        #3 o(mn)
        #maybe we can do it one pass. 
        #what if we do a dictionary to a tuple of sets. We can see the row, column, and grid each appears on with o(1) runtime
        
        #need a way to store grid number. 3* the i box + j box

        # 3 * i // 3 + j//3
        mydict = defaultdict(lambda : (set(), set(), set()))
        #row of tuple, then col of tuple, then index of tuple 
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                row = i
                col = j 
                corner = 3 * (i//3) + j//3
                currval = board[i][j]
                if currval in mydict:
                    if row in mydict[currval][0] or col in mydict[currval][1] or corner in mydict[currval][2]:
                        return False
                
                mydict[currval][0].add(row)
                mydict[currval][1].add(col)
                mydict[currval][2].add(corner)
        return True
                    
        