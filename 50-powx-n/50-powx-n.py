class Solution:
    def __init__(self):
        self.opt = {0 : 1}
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return self.opt[n]
        if n==1:
            self.opt[1] = x
            return self.opt[n]
        if n==-1:
            self.opt[-1] = 1/x
            return self.opt[n]
        
        if n%2==0:
            if n/2 not in self.opt:
                self.opt[n/2] = self.myPow(x,n/2)
            return self.opt[n/2]*self.opt[n/2]
        else:
            if (n+1)/2 not in self.opt:
                self.opt[(n+1)/2]  = self.myPow(x,(n+1)/2)
            if n//2 not in self.opt:
                self.opt[n//2]  = self.myPow(x,n//2)
            
            return self.opt[(n+1)/2]*self.opt[n//2]
    
       