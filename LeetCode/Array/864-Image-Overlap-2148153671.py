class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n=len(img1)
        maxi=0
        for row_shift in range(-(n-1),n):
            for col_shift in range(-(n-1),n):
                overlap=0
                for i in range(n):
                    for j in range(n):
                        new_row=i+row_shift
                        new_col=j+col_shift
                        if 0<=new_row<n and 0<=new_col<n:
                            if img1[i][j]==1 and img2[new_row][new_col]==1:
                                overlap+=1
                maxi=max(maxi,overlap)
        return maxi
        