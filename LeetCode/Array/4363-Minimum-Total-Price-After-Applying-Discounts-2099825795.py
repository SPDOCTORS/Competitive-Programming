class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort()
        discounts.sort()
        total=0
        if len(discounts)>len(prices):
            discounts=discounts[len(discounts)-len(prices):]
        start=len(discounts)-len(prices)
        total+=sum(prices[:len(prices)-len(discounts)])
        for i in range(len(discounts)):
            p=prices[len(prices)-len(discounts)+i]
            d=discounts[i]
            finalprice=(p*(100-d))/100
            total+=finalprice
        return total
        
        