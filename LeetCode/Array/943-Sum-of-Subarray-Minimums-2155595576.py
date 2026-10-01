class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        n=len(arr)
        stack=[]
        left=[0]*n
        right=[0]*n
        mod=10**9+7
        contribution=0
        for i in range(n):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if not stack:
                left[i]=-1
            else:
                left[i]=stack[-1]
            stack.append(i)
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]]>arr[i]:
                stack.pop()
            if not stack:
                right[i]=n
            else:
                right[i]=stack[-1]
            stack.append(i)
            left_choice=(i-left[i])
            right_choice=(right[i]-i)
            contribution+=arr[i]*(i-left[i])*(right[i]-i)
        return contribution%mod
        