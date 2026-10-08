"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #intervals consisting of start and end times
        #first intuition is to obviously sort. 
        #we can track the opened and closed rooms. 
        
        #sort based on open times. 
        #when we open a new room, we want to see what other (how many) rooms are opened at this time and closed at this current time
        #to see wats not closed, we need to have the close times. If a time is less than the curr open time, we close it
        #we need a way to sort or see the closed times -> heap time, each open will be o(logn) and close will be o(n)
        #this runtime is o(nlogn for sort anyways), so when we iterate through it and do n iteration and logn heapify, its not too bad
        #any way we can make each iteration o(n)?
        #maybe if we go through the array


        #1)sort the array by start
        #2)then we will create a varaible for max rooms needed = 0
        #3)create heap
        #4)iterate through the array
        #5)take the start time. 
        #6)go through the top of the heap, if empty leave, if not keep removing all the values less than (or equal) to it
        #7)for every removal subtract one from currRoms. 
        #8)then add our endtime to the heap. 
        #9) if currrooms is greater than maxrooms, replace
        #10) return currromms


        intervals.sort(key = lambda x : x.start)
        maxRoomsNeeded = 0
        currRoomsNeeded = 0
        activeRoomsHeap = []

        for interval in intervals:
            currStart = interval.start
            currEnd = interval.end
            while activeRoomsHeap and currStart >= activeRoomsHeap[0]:
                heapq.heappop(activeRoomsHeap)
                currRoomsNeeded -= 1
            heapq.heappush(activeRoomsHeap, currEnd)
            currRoomsNeeded += 1
            if currRoomsNeeded > maxRoomsNeeded:
                maxRoomsNeeded = currRoomsNeeded
        
        return maxRoomsNeeded

