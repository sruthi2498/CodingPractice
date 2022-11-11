class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        count = 0
        while i<n:
            j = i+1
            start = j
            while j<n and nums[j]==nums[i]:
                nums[j] = "x"
                j+=1
            i = j
        # print(nums)
        
        i = 0
        count = 0
        j = -1
        while i<n:
            while i<n and nums[i]!="x":
                i+=1
                count+=1
            if j<i:
                j = i+1
            while j<n and nums[j]=="x":
                j+=1
            if i<n and j<n:
                nums[i] = nums[j]
                count+=1
                nums[j] = "x"
            i+=1
        # print(nums) 
        # print(count)
        return count
        