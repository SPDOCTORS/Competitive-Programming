class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fraud=sorted(set(nums))
        nums[:len(fraud)]=fraud
        return len(fraud)
        