class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n=len(nums)
        ans=[-1]*n
        st=[]
        for i in range(2*n-1,-1,-1):
            ind=i%n
            cur=nums[ind]
            while st and st[-1]<=cur:
                st.pop()
            if not st:
                ans[ind]=-1
            else:
                ans[ind]=st[-1]
            st.append(cur)
        return ans
        