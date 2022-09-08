class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diffs = [[a[1]-a[0],i] for i,a in enumerate(costs)]
        diffs.sort(key = lambda x : x[0])
        n = len(costs)//2
        total = 0
        for i in range(n):
            index =diffs[i][1] 
            total+=costs[index][1]
        for i in range(n):
            index = diffs[n+i][1] 
            total+=costs[index][0]
        return total