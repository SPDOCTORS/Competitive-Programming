class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        res=[]
        for c in s:
            if c=="(":
                if len(stack)>=1:
                    res.append("(")
                stack.append("(")
            else:
                if len(stack)>=2:
                    res.append(")")
                stack.pop()
        return "".join(res)
            
        