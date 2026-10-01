class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        result=prices.copy()
        st=[]
        for i in range(len(prices)-1,-1,-1):
            while st and prices[st[-1]]>prices[i]:
                st.pop()
            if st:
                result[i]=prices[i]-prices[st[-1]]
            st.append(i)
        return result

        