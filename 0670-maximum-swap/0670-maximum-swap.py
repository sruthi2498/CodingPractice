class Solution:
    def getDigits(self,num):
        digits = []
        while num:
            digits.append(num%10)
            num = num//10
        digits.reverse()
        return digits
        
    def getNum(self,digits):
        num = 0
        n = len(digits)
        i = n-1
        k = 0
        while i>=0:
            num = num + (digits[i] * (10**k))
            k+=1
            i-=1
        return num
        
    def maximumSwap(self, num: int) -> int:
        digits = self.getDigits(num)
        n = len(digits)
        maxs = []
        i = n-1
        maxSoFar = -math.inf
        while i>=0:
            if digits[i]>maxSoFar:
                maxSoFar  = digits[i]
                index = i
            maxs.append([maxSoFar,index])
            i-=1
        
        maxs.reverse()
        # print(digits)
        print(maxs)
        mins= []
        i = 0
        minSoFar = math.inf
        while i<n:
            if digits[i]<minSoFar:
                minSoFar  = digits[i]
                index = i
            mins.append([minSoFar,index])
            i+=1
        print(mins)
        
        i = 0
        maxDiff = -math.inf
        swapi,swapj = None,None
        
        maxNum = -math.inf
        while i<n:
            rightMax,maxIndex = maxs[i]
            leftMin,minIndex = mins[i]
            diff = rightMax - leftMin
            if diff>0:
                swapi,swapj = maxIndex,minIndex
                # maxDiff = diff
                digits[swapi],digits[swapj] = digits[swapj],digits[swapi]
                maxNum = max(maxNum, self.getNum(digits))
                digits[swapi],digits[swapj] = digits[swapj],digits[swapi]
            i+=1
#         print(maxDiff, swapi,swapj)
#         if swapi is not None and swapj is not None:
#             digits[swapi],digits[swapj] = digits[swapj],digits[swapi]
            
        # print(digits)
        # return getNum(digits)
        return maxNum if maxNum>-math.inf else num
        