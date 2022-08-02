from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = Counter(nums)
        val = 0
        i = 0
        while val<=2:
            while counts[val]>0:
                counts[val]-=1
                nums[i]=val
                i+=1
            val+=1
        
        