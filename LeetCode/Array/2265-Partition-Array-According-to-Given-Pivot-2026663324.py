class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lesser,equal,greater=[],[],[]
        for num in nums:
            if pivot>num:
                lesser.append(num)
            elif pivot==num:
                equal.append(num)
            else:
                greater.append(num)
        return lesser+equal+greater
                
        