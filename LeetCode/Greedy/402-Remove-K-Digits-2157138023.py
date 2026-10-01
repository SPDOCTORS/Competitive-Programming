class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[]
        for digit in num:
            while st and k>0 and st[-1]>digit:
                st.pop()
                k-=1
            st.append(digit)
        while k>0:
            st.pop()
            k-=1
        return "".join(st).lstrip("0") or "0"

        