from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k>=n:
            return 0
        counter = Counter(arr)
        counter = [ [c,counter[c]] for c in counter ]
        counter = sorted(counter, key = lambda x :x[1])
        
        removed = 0
        i = 0
        m = len(counter)
        while i<m and removed<k:
            # print(removed,counter)
            _,count = counter[i]
            diff = k - removed
            diff = min(diff,count)
            removed = removed+diff
            counter[i][1] -= diff
            i+=1
        remaining = 0
        # print(counter)
        for i in range(m):
            _,count = counter[i]
            if count>0:
                remaining +=  1
        return remaining
            
        