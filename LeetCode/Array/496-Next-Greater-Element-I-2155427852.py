class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n=len(nums2)
        st=[]
        mp={}
        for i in range (n-1,-1,-1):
            cur=nums2[i]
            while st and st[-1]<=cur:
                st.pop()
            if not st:
                mp[cur]=-1
            else:
                mp[cur]=st[-1]
            st.append(cur)
        ans=[]
        for x in nums1:
            ans.append(mp[x])
        return ans

        