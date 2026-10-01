class Solution:
    def processStr(self, s: str) -> str:
        result=[]
        n=len(s)
        for i in range(n):
            if (s[i]=='*'):
                if result:
                    result.pop()
            elif (s[i]=='#'):
                    result.extend(result)
            elif (s[i]=='%'):
                result=result[::-1]
            else:
                result.append(s[i])
        return "".join(result)