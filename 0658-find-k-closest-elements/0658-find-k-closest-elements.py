from heapq import heappush, heappop, heapify
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diffs = []
        for i,elem in enumerate(arr):
            heappush(diffs, (abs(elem-x),i))
        result = []
        for _ in range(k):
            index = heappop(diffs)[1]
            result.append(arr[index])
        return sorted(result)
        