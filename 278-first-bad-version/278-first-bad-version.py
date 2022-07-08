# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        s = 1
        lastBad = n
        found = False
        while s<=lastBad:
            # print(s,lastBad)
            ind = (lastBad+s)//2
            if isBadVersion(ind):
                if ind==1 or (ind>1 and not isBadVersion(ind-1)):
                    return ind
                lastBad = ind
            else:
                s = ind+1
        return -1