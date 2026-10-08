class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #array of temperatures where i is the temperature on the ith day
        #return result, where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day, return zero
       #[38,30,31 36,40,28]
       #we keep going up 
       # 38 


        #what if we track the total stack adds and then we give each stack value an idx




        #have a stack of all intermediaries, every number in between in the stack will be less than the new number
        #now we can think about intermediaries themselves
        #so lets say we have the stack. If he new number is greater than the number on the stack, we pop. Then, we can add to the stack
        #we can use a dictionary to track the number of pops to see how far we are. We have to use the index number to see because there could be temperature repeats though, so we would store the tuple in s atack
  #temp, stackidx, actualidx
        ret = [0] * len(temperatures)
        mystack = []
        mystack.append((temperatures[0], 0))
        for i in range(1, len(temperatures)):
            while mystack and temperatures[i] > mystack[len(mystack)-1][0]:
                temperature, arridx = mystack.pop()
                ret[arridx] = i - arridx
            mystack.append((temperatures[i], i))
        return ret
