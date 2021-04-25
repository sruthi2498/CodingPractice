package arrays;

/*
You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y). 
You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi). 
A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.

Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location. 
If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.

The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).
*/
public class NearestPoint {

    public static int distance(int x1, int y1, int x2, int y2){
        return Math.abs(x1-x2) + Math.abs(y1-y2);
    }

    public static int nearestValidPoint(int x, int y, int[][] points) {
        int result = -1;
        int minDist = 100000;
        int x2,y2,dist;
        int index = 0;
        for(int[] point : points){
            x2 = point[0];
            y2 = point[1];
            if(x2==x || y2==y){
                dist = minDist;
                if(x2 == x & y2 == y){
                    dist = 0;
                }
                else if(x2 == x){
                    dist = Math.abs(y2-y);
                }
                else if(y2 == y){
                    dist = Math.abs(x2-x);
                }
        
                if(dist<minDist){
                    minDist = dist;
                    result = index;
                }
            }
            index +=1;
        }
        return result;
    }

    public static void main(String args[]) // static method
    {
        // x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
       int x = 3;
       int y = 4;
       int[][] points = {
            {1,2},{3,1},{2,4},{2,3},{4,4}
       };

    
        System.out.println("Result = "+ nearestValidPoint(x,y,points));
    }
}
