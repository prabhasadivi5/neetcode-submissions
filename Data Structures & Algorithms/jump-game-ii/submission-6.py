class Solution:
    def jump(self, nums: List[int]) -> int:
        #array of integers nums where nums[i] is the max length of a jump
        #minimum jumps to reach the last position in the array
        #always a valid answer is assumed
        #at any given index, we know that the number of min jumps is the min of the value from the range i.. i+n
        #If we calculate backwards, we could do O(n). Basically, we start at the end, work back, and each is up to o(n) based on jump length. This is o(n)^2 total runtime

        #nums = [2,4,,1,1,1]
        #jumps = [5,1, 3, 2, 1, 0]
        #will the value after always be less?  
        #so basically, to optimize even lower, we need a way to store -> how do we calculate the minimum from i+n. 
        #the original approach of looking at everything is o(n)
        #there could be a property that we are missing. maybe we can store something like max jump distance? 
        #what if we start from the beginning. We can say 
        #will a location behind always be 
        #can do this recursively by storing the array. But if its already visited, we can store it as negative. 
        # nums[0] = min nums[1], nums[2]. if nums[0]

        #calc the distance to the current jumpmax
        #then within this currentjump max, calculate the distance to the secondjumpmax
        #then keep the counter the number of jumps
        #jumps of the last index


        #[1,4,1,1,1,1]

        #nextjump = 0
        #currjump = nums[0]
        #currjump = 2
        #nextjump = 4
        #currjump = 1
        #nextjump = max(3,1) = 3
        #currjump = 0
        #so, currjump = nextjump
        #nextjump = 0
        #if currjump and nextjump are 0
        #if currjump = 0, iterations goes up by 1
        totaljumps = 1
        nextjumps = 0
        currjumps = nums[0]
        if len(nums) == 1:
            return 0
        for i in range(1, len(nums)):
            currjumps -= 1
            if i == len(nums) - 1:
                break
            nextjumps = max(nextjumps - 1, nums[i])
            if currjumps == 0:
                totaljumps += 1
                currjumps = nextjumps
                nextjumps = 0
        return totaljumps
        
            



        