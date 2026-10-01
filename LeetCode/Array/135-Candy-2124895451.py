class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        if n==0:
            return 0
        left=[1]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                left[i]=left[i-1]+1
        cur=1
        right=1
        sumi=max(1,left[n-1])
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                cur=right+1
            else:
                cur=1
            right=cur
            sumi+=max(left[i],cur)
        return sumi
        