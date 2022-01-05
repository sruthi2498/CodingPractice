class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <2:
            return n
        prevDiff = nums[1]-nums[0]
        count = 1 if prevDiff == 0 else 2
        
        for i in range(2,n):
            diff = nums[i]-nums[i-1]
            if (prevDiff>=0 and diff<0) or (prevDiff<=0 and diff>0):
                count+=1
                prevDiff = diff
        return count
            
                
        
            
        
                
                
        
        