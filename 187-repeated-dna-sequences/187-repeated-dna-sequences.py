from collections import Counter
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        substrings = [s[i:i+10] for i in range(n-9)]
        counter = Counter(substrings)
        result = []
        for k,v in counter.items():
            if v>1:
                result.append(k)
        return result