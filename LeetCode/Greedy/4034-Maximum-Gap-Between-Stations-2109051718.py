class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        left=[]
        right=[]
        j=0
        for ch in skill:
            while station[j]!=ch:
                j+=1
            left.append(j)
            j+=1
        right=[]
        j=len(station)-1
        for ch in reversed(skill):
            while station[j]!=ch:
                j-=1
            right.append(j)
            j-=1
        right.reverse()
        ans=0
        for i in range(len(skill)-1):
            gap=right[i+1]-left[i]
            ans=max(ans,gap)
        return ans
        
        
        