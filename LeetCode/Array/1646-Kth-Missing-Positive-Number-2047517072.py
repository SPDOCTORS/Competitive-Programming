class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        prev=0
        for num in arr:
            miss=num-prev-1
            if k<=miss:
                return prev+k
            k-=miss
            prev=num
        return prev+k
        