class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        pair={}
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            elif s[i]==")":
                opening=stack.pop()
                pair[opening]=i
                pair[i]=opening
        i=0
        direction=1
        result=[]
        while 0<=i<len(s):
            if s[i]=="(" or s[i]==")":
                i=pair[i]
                direction=-direction
            else:
                result.append(s[i])
            i+=direction
        return "".join(result)

        