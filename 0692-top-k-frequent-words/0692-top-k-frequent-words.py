from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        counter = sorted(counter.items(), key = lambda x : x[0])
        counter = sorted(counter, key = lambda x : x[1], reverse = True)[:k]
        # print(counter)
        return [k[0] for k in counter]