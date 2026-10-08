class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #array of people where people[i] is the weight of the ith person
        #infinite number of boats where each boat can carry a max limit
        #each boat carries max two people (if less than limit)
        #min number of boats to carry every person
        #idea is to use a greedy algorithm
        #the algorithm i have is o(n^2), where we start with the heaviest person, and then work our way down. We can use a binary search to find the closest number that is less than the target. 
      #  [5,1,4,2]
      # [1,2,4,5]
      #[1,2,4]
      #also use a hashset to store used 
      #if we cant store anything, we are out
      #pair heaviest witht he lightest. If they can, ship them off
        people.sort()
        lightidx = 0
        heavyidx = len(people) - 1
        boats = 0
        while lightidx <= heavyidx:
            if heavyidx == lightidx: 
                boats += 1
                heavyidx += 1
                break
            else:
                if people[heavyidx] + people[lightidx] <= limit:
                    heavyidx -= 1
                    lightidx += 1
                    boats+= 1
                    continue
                else:
                    heavyidx -= 1
                    boats += 1
                    continue
        return boats
    