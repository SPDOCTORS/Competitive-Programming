class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        n,m=len(s),len(t)
        j=0
        left=[-1]*n
        for i in range(n):
            while j<m and t[j]!=s[i]:
                j+=1
            if j==m:
                break
            left[i]=j
            j+=1
        if left[n-1]!=-1:
            return True
        right=[-1]*n
        j=m-1
        for i in range(n-1,-1,-1):
            while j>=0 and t[j]!=s[i]:
                j-=1
            if j<0:
                break
            right[i]=j
            j-=1
        for i in range(n):
            if i>0 and left[i-1]==-1:
                continue
            if i<n-1 and right[i+1]==-1:
                continue
            L=-1 if i==0 else left[i-1]
            R=m if i==n-1 else right[i+1]
            if L<R-1:
                return True
        return False
        



        
        