class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        pairs=[]
        n=len(arr)
        for i in range(n):
            pairs.append((arr[i],i))
        pairs.sort()
        ans=[0]*n
        rank=1
        ans[pairs[0][1]]=1
        for i in range(1,n):
            if pairs[i][0]!=pairs[i-1][0]:
                rank+=1
            ans[pairs[i][1]]=rank
        return ans
        