class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        count = 0
        i = 0
        currAvg = 0
        currSum = 0
        while i<k:
            currSum+=arr[i]
            i+=1
        currAvg = currSum/k
        if currAvg>=threshold:
            count+=1
        print("currAvg = ",currAvg)
        while i<n:
            end = arr[i]
            start = arr[i-k]
            # print("start = ",start, "end = ",end)
            # print("currAvg = ",currAvg)
            currAvg = currAvg - (start/k) + (end/k)
            if currAvg>=threshold:
                count+=1
            i+=1
        return count
            