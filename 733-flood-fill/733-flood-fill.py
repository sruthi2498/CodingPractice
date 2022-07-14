class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        
        stack = [(sr,sc)]
        startColor = image[sr][sc]
        visited = set()
        toBeColored = []
        while len(stack) > 0 :
            # print(stack)
            i,j = stack.pop(0)
            if image[i][j]==startColor:
                # print(i,j)
                toBeColored.append([i,j])
            visited.add((i,j))
            if i-1>=0 and image[i-1][j]==startColor and (i-1,j) not in visited:
                stack.append([i-1,j])
            if i+1<n and image[i+1][j]==startColor and (i+1,j) not in visited:
                stack.append([i+1,j])
            if j-1>=0 and image[i][j-1]==startColor and (i,j-1) not in visited:
                stack.append([i,j-1])
            if j+1<m and image[i][j+1]==startColor and (i,j+1) not in visited:
                stack.append([i,j+1])
        for i,j in toBeColored:
            image[i][j] = color
        return image
                