class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #can just binary search the 2d matrix. 
        #the index can be calculated by row*size column + column #
        #we can then extract row col using division round down and mod
        
        leftidx = 0
        rightidx = len(matrix[0]) * len(matrix) - 1



        while leftidx <= rightidx:
            mid = (leftidx + rightidx) //2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])

            midval = matrix[row][col]

            if midval == target:
                return True
            
            elif midval < target:
                leftidx = mid + 1
                continue
            else:
                rightidx = mid - 1
                continue
            return True
        return False

        