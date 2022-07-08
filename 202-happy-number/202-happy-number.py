class Solution:
    def __init__(self):
        self.seen = set()
    def sumOfDigits(self,n):
        s = 0
        while n>=1:
            # print(n%10, (n%10) ** 2)
            s+= (n%10)**2
            n = n//10
        return s
        
    def isHappy(self, n: int) -> bool:
        self.seen.add(n)
        m = self.sumOfDigits(n)
        if m==1:
            return True
        if m in self.seen:
            return False
        else:
            return self.isHappy(m)