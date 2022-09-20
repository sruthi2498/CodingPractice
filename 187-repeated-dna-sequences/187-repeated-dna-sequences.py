from collections import Counter
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        counter = {}
        i = 0
        while i+9<n:
            j = i+10
            substring = s[i:j]
            if substring not in counter:
                counter[substring] = 0
            counter[substring]+=1
            i+=1
            
        
        
        # substrings = [s[i:i+10] for i in range(n-9)]
        # counter = Counter(substrings)
        result = []
        for k,v in counter.items():
            if v>1:
                result.append(k)
        return result