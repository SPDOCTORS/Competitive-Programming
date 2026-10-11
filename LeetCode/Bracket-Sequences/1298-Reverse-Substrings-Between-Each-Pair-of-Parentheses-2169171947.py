class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for c in s:
            if c==")":
                result=[]
                while stack and stack[-1]!="(":
                    result.append(stack.pop())
                stack.pop()
                for ch in result:
                    stack.append(ch)
            else:
                stack.append(c)
        return "".join(stack)
        