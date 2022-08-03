class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==1:
            return ["()"]
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
        return list(result)
        