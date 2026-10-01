from collections import defaultdict,Counter
class Solution:
    def maximumWidth(self, planks: list[int]) -> int:
        freq=Counter(planks)
        wid=defaultdict(int,freq)
        ans=max(freq.values())
        vals=sorted(freq)
        for i,a in enumerate(vals):
            for b in vals[i:]:
                if a==b:
                    wid[a+b]+=freq[a]//2
                else:
                    wid[a+b]+=min(freq[a],freq[b])
                ans=max(ans,wid[a+b])
        return ans
        