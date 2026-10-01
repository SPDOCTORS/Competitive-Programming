class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        st = set()
        for i in range(n):
            for j in range(i + 1, n):
                hashset = set()
                for k in range(j + 1, n):
                    summ = nums[i] + nums[j] + nums[k]
                    fourth = target - summ
                    if fourth in hashset:
                        temp = sorted([nums[i], nums[j], nums[k], fourth])
                        st.add(tuple(temp))
                    hashset.add(nums[k])
        ans = [list(t) for t in st]
        return ans

        
        