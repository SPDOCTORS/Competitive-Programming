class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=[]
        depth=0
        for c in s:
            if c=="(":
                depth+=1
                if depth>=2:
                    res.append("(")
            else:
                depth-=1
                if depth>=1:
                    res.append(")")

        return "".join(res)
            
        