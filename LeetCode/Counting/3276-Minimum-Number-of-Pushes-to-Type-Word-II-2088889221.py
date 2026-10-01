class Solution:
    def minimumPushes(self, word: str) -> int:
        count=[0]*26
        ans=0
        for ch in word:
            count[ord(ch)-ord('a')]+=1
        des=sorted(count,reverse=True)
        for i in range(26):
            if des[i]==0:
                break
            ans+=(i//8+1)*des[i]
        return ans


        


        