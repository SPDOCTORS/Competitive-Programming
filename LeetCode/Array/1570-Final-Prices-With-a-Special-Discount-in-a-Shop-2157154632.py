class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        n=len(prices)
        result=prices.copy()
        for i in range(n):
            for j in range(i+1,n):
                if prices[j]<=prices[i]:
                    result[i]=prices[i]-prices[j]
                    break
        return result

        