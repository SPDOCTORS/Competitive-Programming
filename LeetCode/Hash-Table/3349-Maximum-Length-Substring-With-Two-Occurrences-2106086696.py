class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n=len(s)
        freq={}
        left=0
        ans=0
        maxi=float('-inf')
        for right in range(n):
            if s[right] not in freq:
                freq[s[right]]=1
            else:
                freq[s[right]]+=1
            while freq[s[right]]>2:
                freq[s[left]]-=1
                left+=1
            ans=right-left+1
            maxi=max(ans,maxi)
        return maxi
            
        