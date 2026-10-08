class MinStack:

    def __init__(self):
        self.currstack = []
        self.minstack = []

        

    def push(self, val: int) -> None:
        self.currstack.append(val)
        if len(self.minstack) == 0 or self.minstack[len(self.minstack) - 1] >= val:
            self.minstack.append(val)
        

    def pop(self) -> None:
        lastval = self.currstack.pop()
        print(lastval)
        
        if self.minstack[len(self.minstack) - 1] == lastval:
            self.minstack.pop()
        

    def top(self) -> int:
        return self.currstack[len(self.currstack) - 1]
        

    def getMin(self) -> int:
        return self.minstack[len(self.minstack) - 1]
        








#we can just keep another stack and add the min of this at all times
#this is because we have to remove everything else. 
#use an array. To push, we just remove from the last index of the array
#to pop we view the last index of the array
#top pop we first check the length, if there is nothing, we return -> dont need to worry
#getmin -> minimum element. -> we can store the min but what if it gets removed from the stack?

#if we reove the smallest element from the stack and then call min() what do we do. 
#first intuition is to call a heap -> heappush is logn, so too slow. What if we use a stack to track the min. if we smallerthan the top, then goes in one. If bigger than the top it goes in another. 
#what if we have two deques. 
#the first one keeps adding the smallest to the top. biggest to the bottom. 
#if we use a linkedlist and maybe a dictionary, we dont know what values its between 