class Solution:
    def __init__(self):
        self.pars = {1:["()"]}
    def generateParenthesis(self, n: int) -> List[str]:
        if n in self.pars:
            return self.pars[n]
        result = set()
        for i in range(1,n):
            # print(i,n-i)
            first = self.generateParenthesis(i) if i not in self.pars else self.pars[i]
            second = self.generateParenthesis(n-i) if n-i not in self.pars else self.pars[n-i]
            for f in first:
                for s in second:
                    result.add(f+s)
        prev = self.generateParenthesis(n-1) if n-1 not in self.pars else self.pars[n-1]
        for p in prev:
            result.add("("+p+")")
         
        self.pars[n] = list(result)
        return self.pars[n]
        