class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        st=[]
        n=len(nums)
        left=[0]*n
        right=[0]*n
        maxi=0
        mini=0
        contribution=0
        for i in range(n):
            while st and nums[st[-1]]<=nums[i]:
                st.pop()
            if not st:
                left[i]=-1
            else:
                left[i]=st[-1]
            st.append(i)
        st=[]
        for i in range(n-1,-1,-1):
            while st and nums[st[-1]]<nums[i]:
                st.pop()
            if not st:
                right[i]=n
            else:
                right[i]=st[-1]
            st.append(i)
            left_choice=(i-left[i])
            right_choice=(right[i]-i)
            contribution=nums[i]*left_choice*right_choice
            maxi+=contribution
        st=[]
        for i in range(n):
            while st and nums[st[-1]]>=nums[i]:
                st.pop()
            if not st:
                left[i]=-1
            else:
                left[i]=st[-1]
            st.append(i)
        st=[]
        for i in range(n-1,-1,-1):
            while st and nums[st[-1]]>nums[i]:
                st.pop()
            if not st:
                right[i]=n
            else:
                right[i]=st[-1]
            st.append(i)
            left_choice=i-left[i]
            right_choice=right[i]-i
            contribution=nums[i]*left_choice*right_choice
            mini+=contribution
        return maxi-mini
    
        