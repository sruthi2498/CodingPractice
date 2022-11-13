from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if groupSize>n or n%groupSize!=0:
            return False
        hand.sort()
        counter = Counter(hand)
        i = 0
        m = len(counter)
        while i<n:
            # print(counter)
            if counter[hand[i]]>0:
                count = 1
                for card in range(hand[i], hand[i]+groupSize):
                    # print(card)
                    if card not in counter or counter[card]<=0:
                        return False
                    count+=1
                    counter[card]-=1
                    if counter[card]<=0:
                        counter.pop(card)
            i+=1
        return not counter