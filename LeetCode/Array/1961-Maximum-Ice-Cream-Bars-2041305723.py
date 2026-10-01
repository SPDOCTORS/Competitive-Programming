class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if not costs:
            return costs
        max_val=max(costs)
        count=[0]*(max_val+1)
        for cost in costs:
            count[cost]+=1
        result=0
        for i in range(len(count)):
            while count[i]>0 and coins>=i:
                coins-=i
                result+=1
                count[i]-=1
        return result
        