class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefixSum = arr[0]
        # oddsum = [True if arr[0]%2!=0 else False]
        n = len(arr)
        oddSumCount = 0
        evenSumCount = 0
        if arr[0]%2==0:
            evenSumCount+=1
        else:
            oddSumCount+=1
            
        count = oddSumCount
        
        for i in range(1,n):
            prefixSum+=arr[i]
            if prefixSum%2!=0:
                oddSumCount+=1
                count+=1
                count+=evenSumCount
            else:
                evenSumCount+=1
                count+=oddSumCount
            # print(prefixSum)
            # print(oddSumCount,evenSumCount,count)
        # print(prefixSum,oddsum)
          
        # count = 0
        # for i in range(n):
        #     for j in range(i+1):
        #         if j==0  and oddsum[i]:
        #             count+=1
        #         elif j>0 and ((oddsum[i] and not oddsum[j-1]) or (not oddsum[i] and oddsum[j-1])):
        #             count+=1
        #         # print(j,i,count)
        return count%1000000007