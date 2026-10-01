class Solution:
    def maxelement(self,arr,col):
        n=len(arr)
        max_val=float('-inf')
        index=-1
        for i in range(n):
            if arr[i][col]>max_val:
                max_val=arr[i][col]
                index=i
        return index
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n=len(mat)
        m=len(mat[0])
        low,high=0,m-1
        while low<=high:
            mid=low+(high-low)//2
            row=self.maxelement(mat,mid)
            left=mat[row][mid-1] if mid>0 else float('-inf')
            right=mat[row][mid+1] if mid+1<m else float('-inf')
            if mat[row][mid]>left and mat[row][mid]>right:
                return[row,mid]
            elif left>mat[row][mid]:
                high=mid-1
            else:
                low=mid+1
        return [-1,-1]        