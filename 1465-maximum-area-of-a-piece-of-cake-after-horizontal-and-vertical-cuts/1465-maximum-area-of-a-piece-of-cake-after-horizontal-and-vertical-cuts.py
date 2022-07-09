class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        maxArea = 0
       
        horizontalCuts.append(h)
        horizontalCuts.sort()
        verticalCuts.append(w)
        verticalCuts.sort()
        horizontalCuts = [horizontalCuts[i]-horizontalCuts[i-1] if i>0 else horizontalCuts[i] for i in range(len(horizontalCuts))]
        verticalCuts = [verticalCuts[i]-verticalCuts[i-1] if i>0 else verticalCuts[i] for i in range(len(verticalCuts))]
        return (max(verticalCuts)*max(horizontalCuts) )%1000000007
                
        
               