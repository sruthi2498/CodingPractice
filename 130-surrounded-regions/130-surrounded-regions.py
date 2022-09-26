class Solution:
    def getNeighb(self,i,j,n,m):
        neighb = []
        if i>0:
            neighb.append((i-1,j))
        if j>0:
            neighb.append((i,j-1))
        
        if i<n-1:
            neighb.append((i+1,j))
        
        if j<m-1:
            neighb.append((i,j+1))
        
        return neighb
    
    def dfs(self,board,n,m):
        visited = set()
        groups = []
        ind = -1
        for i in range(n):
            for j in range(m):
                if board[i][j]=="O" and (i,j) not in visited:
                    groups.append(set())
                    ind+=1
                    stack = [(i,j)]
                    groups[ind].add((i,j))
                    while stack:
                        x,y = stack.pop()
                        visited.add((x,y))
                        groups[ind].add((x,y))
                        for k,l in self.getNeighb(x,y,n,m):
                            if board[k][l]=="O" and (k,l) not in visited:
                                stack.append((k,l))
        return groups
                                
    
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        groups = self.dfs(board,n,m)
        print(groups)
        
        for group in groups:
            flip = True
            for i,j in group:
                if i==0 or i==n-1 or j==0 or j==m-1:
                    flip = False
                    break
            print(flip)
            if flip:
                for i,j in group:
                    board[i][j]="X"
                        
        
        