class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n=len(heights)
        m=len(heights[0])
        if n==1 and m==1:
            return [[0,0]]
        dirr=[(1,0),(0,1),(-1,0),(0,-1)]
        boolpair= [[[False,False] for _ in range(m)] for _ in range(n)]
        ans=set()

        def startdfs(x,y):
            visited=set()
            
            def dfs(i,j):
                if (i,j) not in visited:
                    visited.add((i,j))

                    for (dx,dy) in dirr:
                        nx,ny=i+dx,j+dy
                        if nx<n and ny<m and nx>=0 and ny>=0:
                            if heights[i][j]>=heights[nx][ny]: # can flow to next
                                dfs(nx,ny)

                            # check if that i,j is near a sea
                            if i==0 or j==0:
                                boolpair[x][y][0]=True
                                if boolpair[x][y][1]==True:
                                    ans.add((x,y))
                                    break
                            if i==(n-1) or j==(m-1):
                                boolpair[x][y][1]=True
                                if boolpair[x][y][0]==True:
                                    ans.add((x,y))
                                    break
            dfs(x,y)

        for i in range(n):
            for j in range(m):
                startdfs(i,j)
        
        return list(list(i) for i in ans)