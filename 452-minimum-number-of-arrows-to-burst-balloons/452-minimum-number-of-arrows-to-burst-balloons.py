class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x : x[1])
        print(points)
        count = 1
        i = 1
        n = len(points)
        start,end = points[0][0],points[0][1]
        while i<n:
            # print(start,end,points[i],count)
            if points[i][0]>end:
                count+=1
                start,end = points[i][0],points[i][1]
            i+=1
        return count