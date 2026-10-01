class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        MOD=10**9+7
        a0=0
        b0=0
        c0=0
        count=0
        for num in nums:
            if num<a:
                a0+=1
                count+=b0+c0
            if a<=num<=b:
                b0+=1
                count+=c0
            if num>b:
                c0+=1
        return count%MOD
        
            

        