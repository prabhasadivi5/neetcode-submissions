class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #break into substrings where every substring is a palindrome. At each spot, we can break or continue. If the substring were on itself is not a palindrome, we break anyways so we backtrack
        #if it is, we have two options -> 1 -> to add it as part of the string and two to make a new string
        ret = []
        #in each function call, we need to track the curr string, the array we have so far and the idx
        def recurse(curr, arr, idx):
            
            #option 1 is to add idx[i] to the current arr and option 2 is to break it
            curr = curr + s[idx]
            if(idx == len(s)  -  1):
                if isPalindrome(curr):
                    arr.append(curr)
                    ret.append(arr.copy())
                    arr.pop()
                    return
                else:
                    return
            if isPalindrome(curr):
                #need end case too (base case)
                print(curr)
                arr.append(curr)
                recurse('', arr, idx + 1)
                arr.pop()

            recurse(curr, arr, idx + 1)

        def isPalindrome(mystr):
            front = 0
            back = len(mystr) - 1
            while (front <= back):
                if mystr[back] != mystr[front]: 
                    return False
                front += 1
                back -= 1
            return True      
        recurse('', [], 0)  
        return ret