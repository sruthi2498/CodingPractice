class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        n = len(arr)
        s = sum(arr)
        print(s)
        if s%3!=0:
            return False
        leftSum = [arr[0]]
        
        for i in range(1,n):
            leftSum.append(leftSum[i-1]+arr[i])
        rightSum=[arr[n-1]]
        for i in range(n-2,-1,-1):
            rightSum.append(rightSum[n-i-2]+arr[i])
        rightSum.reverse()
        print(leftSum)
        print(rightSum)
        for i in range(n):
            if leftSum[i]==s//3:
                j=n-1
                while j>i and rightSum[j]!=s//3:
                    j-=1
                if j<=i+1:
                    return False
                # print(i,j)
                if leftSum[j-1] - leftSum[i]==s//3:
                    return True
                    
        return False
        
        