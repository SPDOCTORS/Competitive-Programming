class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mini=float('inf')
        si=-1
        hash=[0]*256
        for c in t:
            hash[ord(c)]+=1
        count=0
        l,r=0,0
        while r<len(s):
            if hash[ord(s[r])]>0:
                count+=1
            hash[ord(s[r])]-=1
            while count==len(t):
                if r-l+1<mini:
                    mini=r-l+1
                    si=l
                hash[ord(s[l])]+=1
                if hash[ord(s[l])]>0:
                    count-=1
                l+=1
            r+=1
        return s[si:si+mini] if si!=-1 else ""
        