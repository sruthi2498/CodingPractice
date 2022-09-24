
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i<n:
            if i+1<n and nums[i+1]==nums[i]:
                i = i+1
            j = i+1
            while j<n and nums[j]==nums[i]:
                nums[j]="F"
                j+=1
            i = j
        print(nums)
        
        i = 0
        while i<n:
            while i<n and nums[i]!="F":
                i+=1
            # print(i)
            j = i+1
            while j<n and nums[j]=="F":
                j+=1
            if j<n:
                temp = nums[i]
                nums[i]= nums[j]
                nums[j]= temp
                print(nums)
            i +=1
            
        k = 0
        while k<n and nums[k]!="F":
            k+=1
        return k