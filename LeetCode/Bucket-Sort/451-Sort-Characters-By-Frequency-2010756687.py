class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i,char in enumerate(s):
            if char not in d:
                d[char]=1
            else:
                d[char]+=1
        result=sorted(d.keys(),key=lambda ch:(-d[ch],ch))
        ans=""
        for ch in result:
            ans+=ch*d[ch]
        return ans
        