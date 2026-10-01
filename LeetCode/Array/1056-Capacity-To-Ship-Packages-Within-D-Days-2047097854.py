class Solution:
    def poss(self,weights,capacity):
        req=1
        curr_load=0
        for w in weights:
            if curr_load+w>capacity:
                req+=1
                curr_load=0
            curr_load+=w
        return req
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low,high=max(weights),sum(weights)
        while low<=high:
            mid=low+(high-low)//2
            if self.poss(weights,mid)<=days:
                high=mid-1
            else:
                low=mid+1
        return low
        