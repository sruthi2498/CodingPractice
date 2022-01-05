class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x : x[1])
        # print(points)
        count = 1
        i = 1
        n = len(points)
        end = points[0][1]
        while i<n:
            if points[i][0]>end:
                count+=1
                end = points[i][1]
            i+=1
        return count