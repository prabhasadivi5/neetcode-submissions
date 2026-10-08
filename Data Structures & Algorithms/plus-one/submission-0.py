class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #start at the back. if we add and its a 9, we make it a zero and move on. #if we make it to the front and we have a zero, we can push a zero to the back and flip it. 
        #o(n) runtime * 2 
        
        startidx = len(digits) - 1
        for i in range(startidx, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            
            else:
                digits[i] += 1
                break
            


        if digits[0] == 0:
            digits.append(1)
            digits = digits[::-1]
        return digits

        