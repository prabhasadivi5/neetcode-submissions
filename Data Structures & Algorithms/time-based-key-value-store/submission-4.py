#store multiple value for the same key at different timestamps and retrieve the keys value at a certain time. 
#first Idea is to store the keys in a dictionary of arrays. 
#the array is of type tuple. This way, we can sort the array based on time. 
#we then run a binary search on the array to find the time of the largest set before n. 
#the runtime of this is o(logn)
#timestamps of set are strictly increasing so we dont have to sort the array every time

#of items * additions/item is the storage
#set is o(1)
#get is o(logn) where n is the number of sets
#lets see if there is a faster way to get a value before a timestamp. 
#heap -> pop is n, but we might have to pop up to n times to get what we want
#stack -> again up to n pops 
#most likely we will have to use a dictionary to an array and then binary search


class TimeMap:

    def __init__(self):
        self.ValsTupleDict = defaultdict(list)

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ValsTupleDict[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        currTimeline = self.ValsTupleDict[key]
        if len(currTimeline) == 0 or timestamp < currTimeline[0][0]:
            return ""
        leftptr = 0
        rightptr = len(currTimeline) - 1
        mid = (leftptr + rightptr + 1)//2
        while leftptr < rightptr:
            midTime = currTimeline[mid][0]
            if timestamp == midTime: 
                return currTimeline[mid][1]
            if timestamp > midTime:
                leftptr = mid 
            elif timestamp < midTime:
                rightptr = mid - 1
            
            mid = (leftptr + rightptr + 1)//2
        
        return currTimeline[leftptr][1]
            
            

        # 1 2   4  7 9  10 12 13
        #1 2    4   7 11  7 11
                    
        #if timestamp == mid -> we just return that value.
        #if timestamp < mid right == mid  (cant include mid because its after)
        #if timestamp > mid: left = mid + 1
        #if left == right -> return the one before 
        

       
