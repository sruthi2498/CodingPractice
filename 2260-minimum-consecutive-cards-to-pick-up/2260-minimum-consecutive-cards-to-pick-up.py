class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        pos = {}
        minDist = math.inf
        for i,x in enumerate(cards):
            if x not in pos:
                pos[x] = i
            else:
                minDist = min(minDist, i-pos[x]+1)
                pos[x] = i
        if minDist == math.inf:
            return -1
        return minDist