class Solution:
    def minOperations(self, s1: str, s2: str) -> int:
        n=len(s1)
        if n==1 and s1=="1" and s2=="0":
            return -1
        ans=0
        i=0
        while i<n:
            if s1[i]=="0" and s2[i]=="1":
                ans+=1
            elif s1[i]=="1" and s2[i]=="0":
                if i+1<n and s1[i+1]=="1" and s2[i+1]=="0":
                    ans+=1
                    i+=1
                else:
                    ans+=2
            i+=1
        return ans

        