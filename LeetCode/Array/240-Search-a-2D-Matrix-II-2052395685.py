class Solution:
    def bina(self,arr,target):
        low,high=0,len(arr)-1
        while low<=high:
            mid=low+(high-low)//2
            if arr[mid]==target:
                return True
            elif arr[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            if self.bina(matrix[i],target):
                return True
        return False
