class Solution:
    
    def search(self, nums: List[int], target: int, l, r) -> int:
        # print("\tbs ",l,r)
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                l+=1
            else:
                r-=1
        return -1
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        n= len(numbers)
        while i<n :
            # print("i",i)
            remaining = target - numbers[i]
            # print("remaining",remaining, remaining==target/2)
            if remaining==target/2:
                # print("\thlf")
                if i<n-1 and numbers[i+1]==remaining:
                    return [i+1,i+2]
            else:
                start = i+1
                # print("\tstart",start)
                while start<n and numbers[start]==numbers[i]:
                    start+=1
                # print("\tstart",start)
                index = self.search(numbers,remaining, start,n-1)
                # print('\tbs index',index)
                if index!=-1:
                    return[i+1,index+1]
            i=start