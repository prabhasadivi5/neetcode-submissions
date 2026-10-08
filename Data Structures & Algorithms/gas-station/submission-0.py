class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        startidx = 0
        tank = 0
        total = 0

        for i in range(len(gas)):
            difference = gas[i] - cost[i]
            tank += difference
            total += difference

            if tank < 0:
                startidx = i + 1
                tank = 0

        if total < 0:
            return -1

        return startidx