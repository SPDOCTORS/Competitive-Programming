class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n=len(s)
        freq=[0]*26
        for ch in s:
            freq[ord(ch)-ord('a')]+=1
        ans=""
        i=0
        while i<n:
            idx=ord(target[i])-ord('a')
            if freq[idx]>0:
                ans+=target[i]
                freq[idx]-=1
                i+=1
            else:
                break
        if i<n:
            current=ord(target[i])-ord('a')
            for j in range(current+1,26):
                if freq[j]>0:
                    result=ans+chr(ord('a')+j)
                    freq[j]-=1
                    for k in range(26):
                        result+=chr(ord('a')+k)*freq[k]
                    return result
        start=i-1
        for pos in range(start,-1,-1):
            idx=ord(target[pos])-ord('a')
            freq[idx]+=1
            ans=ans[:-1]
            for j in range(idx+1,26):
                if freq[j]>0:
                    result=ans+chr(ord('a')+j)
                    freq[j]-=1
                    for k in range(26):
                        result+=chr(ord('a')+k)*freq[k]
                    return result
        return ""
        