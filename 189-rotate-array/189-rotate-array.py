class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        i = 0
        j = n-1
        while i<=j:
            t = nums[i]
            nums[i]=nums[j]
            nums[j]=t
            i+=1
            j-=1
        print(nums)
        i = 0 
        j = k-1
        while i<=j:
            t = nums[i]
            nums[i]=nums[j]
            nums[j]=t
            i+=1
            j-=1
        print(nums)
        i = k
        j = n-1
        while i<=j:
            t = nums[i]
            nums[i]=nums[j]
            nums[j]=t
            i+=1
            j-=1
        print(nums)