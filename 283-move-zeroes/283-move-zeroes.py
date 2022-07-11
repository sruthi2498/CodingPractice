class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
#         i = 0
#         while i<n and nums[i]==0:
#             i+=1
#         j = i+1
#         while j<n and nums[j]!=0:
#             j+=1
#         t = nums[i]
        zeroC = 0
        i = 0
        while i<n:
            if nums[i]==0:
                zeroC+=1
            i+=1
        
        i = 0
        j = 0
        while i<=n-zeroC:
            while j<n and nums[j]==0:
                j+=1
            if j<n:
                nums[i] = nums[j]
            j+=1
            i+=1 
        print(nums)
        i = n-zeroC
        while i<n:
            nums[i]=0
            i+=1
            
        
        