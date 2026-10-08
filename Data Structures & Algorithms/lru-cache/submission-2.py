from collections import deque
class LRUCache:
    #need to track the size of the capacity
    #if we over the size, remove the most recently used
    #to add we can use a queue, but to search will take up o(n) time to get the value 
    #we can use a dictionary to search up, and then to put, we can remove from the queue
    #this way, a get is o(1) and a put is o(n) which it has to be since we have to ahve a queue to track order 

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mydict = {}
        self.myq = deque()
        self.size = 0

        

    def get(self, key: int) -> int:
        if key in self.mydict: 
            self.myq.remove(key)
            self.myq.append(key)
            return self.mydict[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if not key in self.mydict:
            self.myq.append(key)
            self.mydict[key] = value
            self.size += 1
            if self.size > self.capacity:
                temp = self.myq.popleft()
                self.mydict.pop(temp)
                self.size -= 1
        else:
            self.myq.remove(key)
            self.myq.append(key)
            self.mydict[key] = value
            

    


        
