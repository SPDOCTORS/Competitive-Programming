class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        it_even=False
        it_odd=False
        for x in nums1:
            if x%2==1:
                it_odd=True
            else:
                it_even=True
        if not(it_even and it_odd):
            return True
        return min(nums1)%2==1
        