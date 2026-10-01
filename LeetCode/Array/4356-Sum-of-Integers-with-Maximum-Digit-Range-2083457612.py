class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        maxi=float('-inf')
        ans=0
        for num in nums:
            largest=0
            smallest=9
            temp=num
            while temp>0:
                digit=temp%10
                largest=max(largest,digit)
                smallest=min(smallest,digit)
                temp//=10
            digit_r=largest-smallest

            if digit_r>maxi:
                maxi=digit_r
                ans=num
            elif digit_r==maxi:
                ans+=num
        return ans
        