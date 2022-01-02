import math
class Solution:
    
    def binarySearch(self,val,nums,l,r,n):
        while l<=r:
            mid = l+(r-l)//2
            # print("binarySearch",l,r,mid)
            if nums[mid]>val:
                l = mid+1
            else:
                r = mid-1
        print("binarySearch",l,r,mid)
        l = min(l,n-1)
        r = min(r,n-1)
        l = max(l,0)
        r = max(r,0)
        print("binarySearch",l,r,mid)
        minElem = math.inf
        res=-1
        for i in list(set([l,r,mid])):
            print("binarySearch",minElem,res)
            if nums[i]>val and nums[i]<minElem:
                res = i
                minElem = nums[i]
        return res
        
    
    def reverse(self,nums,l,r):
        i=l
        j = r
        while i<=j:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1
        return nums
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        print(nums)
        n = len(nums)
        if n<2:
            return nums
        i = n-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        if i<=0 and nums[0]>=nums[1]:
            # print("sorted")
            # return sorted(nums)
            nums.sort()
            return
        print(i)
        if i+1==n-1:
            j = i+1
        else:
            j = self.binarySearch(nums[i],nums,i+1,n-1,n)
        print(j)
        nums[i],nums[j] = nums[j],nums[i]
        print(nums,nums[:i+1], nums[i+1:][::-1])
        nums = self.reverse(nums,i+1,n-1)
        
        
        