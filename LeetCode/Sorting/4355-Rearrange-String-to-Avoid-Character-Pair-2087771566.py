class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        y_s=[]
        x_s=[]
        other=[]
        for ch in s:
            if ch==y:
                y_s.append(ch)
            elif ch==x:
                x_s.append(ch)
            else:
                other.append(ch)
        return "".join(y_s+other+x_s)

        