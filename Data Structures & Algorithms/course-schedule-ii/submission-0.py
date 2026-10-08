from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #we are given array prerequesites saying we nede to take b if we want to take a [a,b]
        #total of numCourses required to take numbered from 0 to numcourses - 1
        #return a valid ordering of courses you can take to finish call courses, if many valids, return any
        #not possible return empty array
        #first obviously we need an adjacency matrix
        #then, we have to look for every course with no prerequesites (o(n)) runtime
        #we have to add these to our visited set
        #we then look at every course again, if its prerequesites completed by the visited, we run it. 
        #this is a little slow, o(n^2)
        #what if we keep a deque. 
        #


        # 1 -> 2, 3
        # 2 -> 3
        # 3 -> none 

        #we can also remove from the set everytime, and if the set size is 0, we are able to remove -> each edge being removed once is o(e)
        #if its equal to zero, we can add to the end of the return array.
        #we want to iterate through all of the neighbors of the return array so use both a queue and an array 


        #dict -> set with all of the prereqs
        #queue with all of the visitable courses. 
        #array with all of the fully visited courses
        #we also need a way to see what courses our course is a prerequesite for. We can use another dictionary to a set. backwards so we know where to look in the dictionary 

        #then we first populate queue + array courses with no prereqs
        #top is popq value, we take it, look at what its a prerequisite for, remove that from the prerequesites count. 
        #if that dict is empty now, add that to the queue and array
        #keep going until the queue is empty
        #if the size of the array < n, return empty arr otherwise return 
        

        #from there, we run a dfs starting at that course.  

        prereqsFor = defaultdict(list)
        prereqsLeft = defaultdict(int)
        myq = deque()
        ret = []

        for course, prereq in prerequisites:
            prereqsFor[prereq].append(course)
            prereqsLeft[course] += 1



        for i in range(numCourses):
            if prereqsLeft[i] == 0:
                myq.append(i)
                ret.append(i)


        while myq:
            currclass = myq.popleft()
            for unlockedclass in prereqsFor[currclass]:
                prereqsLeft[unlockedclass] -= 1
                if prereqsLeft[unlockedclass] == 0:
                    myq.append(unlockedclass)
                    ret.append(unlockedclass)
        if len(ret) != numCourses:
            return []
        return ret

        