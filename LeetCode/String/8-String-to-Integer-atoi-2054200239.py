class Solution:
    def myAtoi(self, s: str) -> int:
        i,n=0,len(s)
        while i<n and s[i]==" ":
            i+=1
        sign=1
        if i<n and s[i]=="-":
            sign=-1
            i+=1
        elif i<n and s[i]=="+":
            i+=1
        result=0
        while i<n and s[i].isdigit():
            result=result*10+(ord(s[i])-ord('0'))
            i+=1
            if result*sign>=2**31 -1:
                return 2**31-1
            if result*sign<=-2**31:
                return -2**31
        return result*sign

        