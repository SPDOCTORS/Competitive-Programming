class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        maxl=0
        for i in range(n):
            hash_set=[0]*256
            for j in range(i,n):
                if hash_set[ord(s[j])]==1:
                    break
                hash_set[ord(s[j])]=1
                curr=j-i+1
                maxl=max(maxl,curr)
        return maxl        