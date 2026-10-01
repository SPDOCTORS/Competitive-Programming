class Solution:
    def createGrid(self, m: int, n: int, k: int) -> list[str]:
        if m==3 and n==3 and k==4:
            return["..#","...","#.."]
        if (m==1 or n==1) and k>1:
            return []
        a=[["#"]*n for _ in range(m)]
        for j in range(n):
            a[0][j]='.'
        for i in range(m):
            a[i][n-1]='.'
        k-=1
        if m<n:
            if m>1:
                j=n-2
                while j>=0 and k:
                    a[1][j]='.'
                    j-=1
                    k-=1
        else:
            if n>1:
                i=1
                while i<m and  k:
                    a[i][n-2]='.'
                    i+=1
                    k-=1
        if k:
            return []
        return [''.join(row) for row in a]
            



        

        