class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_b=0
        mini=0
        for c in s:
            if c=="(":
                open_b+=1
            else:
                if open_b>0:
                    open_b-=1
                else:
                    mini+=1
        return open_b+mini

        