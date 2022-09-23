import math
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        while i<n and s[i]==" ":
            i+=1
        if i==n:
            return 0
        neg = False
        sign = False
        if s[i]=="-":
            neg = True
            sign = True
            i+=1
        elif s[i]=="+":
            sign = True
            i+=1
        elif not s[i].isnumeric():
            return 0
        
        if i==n:
            return 0
        if i<n and sign and not s[i].isnumeric():
            return 0
        start = i
        while i<n and s[i].isnumeric():
            i+=1
        # print(s[start:i])   
        num = int(s[start:i])
        # print(num)
        if neg:
            num = -num 
            
        num = min(num, math.pow(2,31)-1)
        num = max(num, math.pow(-2,31))
        return int(num)