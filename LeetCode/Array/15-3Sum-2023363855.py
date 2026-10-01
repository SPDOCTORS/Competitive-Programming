class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplet_set=set()
        n=len(nums)
        for i in range(n):
            hashset=set()
            for j in range(i+1,n):
                third=-(nums[i]+nums[j])
                if third in hashset:
                    temp=[nums[i],nums[j],third]
                    temp.sort()
                    triplet_set.add(tuple(temp))
                hashset.add(nums[j])
        ans=[list(triplet) for triplet in triplet_set]
        return ans

        