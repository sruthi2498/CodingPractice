from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(list(magazine))
        for c in ransomNote:
            if c not in counter:
                return False
            counter[c]-=1
            if counter[c]<=0:
                counter.pop(c)
        return True