class Solution:
    def __init__(self):
        self.map = {"0":[""],"1":[""],"2":["a","b","c"],"3":["d","e","f"], "4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        self.cache = {}
     
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n==0:
            return []
        if n==1:
            return self.map[digits[0]]
        
        res = []
        
        
        for a in self.map[digits[0]]:
            for b in self.letterCombinations(digits[1:]):
                res.append(a+b)
        
        return res
        
        
                    