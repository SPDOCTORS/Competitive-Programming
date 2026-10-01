class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        maxl=0
        l,r=0,0
        mpp={}
        while r<n:
            mpp[fruits[r]]=mpp.get(fruits[r],0)+1
            if len(mpp)>2:
                while len(mpp)>2:
                    mpp[fruits[l]]-=1
                    if mpp[fruits[l]]==0:
                        del mpp[fruits[l]]
                    l+=1
            if len(mpp)<=2:
                maxl=max(maxl,r-l+1)
            r+=1
        return maxl
        