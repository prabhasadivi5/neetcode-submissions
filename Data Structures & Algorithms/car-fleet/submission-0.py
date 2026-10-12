class Solution:
            #n cars trveling to the same destination one a one lane highway
        #we are given two arrays of integers position and speed, both of length n. 
        #position i is position of the ith car
        #speed i is the speed of the ith car. 
        #destination is at position target miles 
        #should be pretty simple. Calculate the time each car arrives at the destination
        #if the time is less than that of the one before it, we store that holding time and move to the next car. 
        #if its greater than, we make a new fleet 
        #this is if its sorted.
        #if its not sorted by position what can we do? 
        #can sort by position and speed 
        #what if we just first calculate arrival time
        #we HAVE to sort based on position. Otherwise its too complicated -> we have to say things like 
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
            fleets = []
            numFleets = 1
            
            for i in range (len(position)):
                fleets.append((position[i], speed[i]))
            fleets.sort(reverse = True)
            currArrival = ((target-fleets[0][0])/fleets[0][1])

            for i in range(1, len(position)):
                newArrival = ((target-fleets[i][0])/fleets[i][1])
                if newArrival <= currArrival:
                    continue
                else:
                    numFleets += 1
                    currArrival = newArrival
            return numFleets



        