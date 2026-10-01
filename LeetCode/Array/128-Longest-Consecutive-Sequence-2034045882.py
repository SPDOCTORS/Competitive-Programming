class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        n=len(nums)
        longest=1
        cnt=1
        s=set()
        for i in range(n):
            s.add(nums[i])
        for itt in s:
            if itt -1 not in s:
                cnt=1
                x=itt
                while x+1 in s:
                    x=x+1
                    cnt=cnt+1
                longest=max(longest,cnt)
        return longest



        