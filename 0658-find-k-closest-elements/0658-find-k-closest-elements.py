from heapq import heappush, heappop, heapify
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                l+=1
            else:
                r-=1
        # print(l,r)
        return max(l,r)
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        n = len(arr)
        if k==n:
            return arr
        pos = self.searchInsert(arr,x)
        pos = max(min(n-1,pos),0)
        print(pos)
        
        if x<arr[pos]:
            print("move pos to left")
            j = pos-1
            moved = False
            while j>=0 and abs(arr[j]-x)<=abs(arr[pos]-x):
                j-=1
                moved = True
            if moved:
                pos = j+1
        elif x>arr[pos]:
            j = pos+1
            moved = False
            while j<n and abs(arr[j]-x)<=abs(arr[pos]-x):
                moved = True
                j+=1
            if moved:
                pos = j-1
        print(pos)
        if pos==0:
            return arr[:k]
        if pos==n-1:
            return arr[n-k:]
        
        start = pos+1-k 
        if start<0:
            start = 0
        end = start+k-1
        found = False
        
        while not found:
            print("start",start,"end",end)
            startDiff,endDiff = abs(arr[start]-x),abs(arr[end]-x)
            print("startDiff",startDiff,"endDiff",endDiff)
            j = end+1
            if j==n:
                found = True
                break
            diff = abs(arr[j]-x)
            print("diff",diff)
            if diff<startDiff or diff<endDiff:
                start+=1
                end+=1
            else:
                found = True
        return arr[start:end+1]