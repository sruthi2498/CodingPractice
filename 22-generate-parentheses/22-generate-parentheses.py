class Solution:
    def __init__(self):
        self.pars = {1:["()"]}
    def generateParenthesis(self, n: int) -> List[str]:
        if n in self.pars:
            return self.pars[n]
        
        result = set()
        prev = self.generateParenthesis(n-1)
        for p in prev:
            result.add("("+p+")")
        
        for i in range(1,n):
            # print(i,n-i)
            first = self.generateParenthesis(i)
            second = self.generateParenthesis(n-i)
            for f in first:
                for s in second:
                    result.add(f+s)
        self.pars[n] = list(result)
        return self.pars[n]
        