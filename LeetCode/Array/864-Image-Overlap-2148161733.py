class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n=len(img1)
        ones1=[]
        ones2=[]
        maxi=0
        for i in range(n):
            for j in range(n):
                if img1[i][j]==1:
                    ones1.append((i,j))
                if img2[i][j]==1:
                    ones2.append((i,j))
        shift=Counter()
        for i1,j1 in ones1:
            for i2,j2 in ones2:
                row_shift=i2-i1
                col_shift=j2-j1
                shift[(row_shift,col_shift)]+=1
        if shift:
            maxi=max(shift.values())
        return maxi



        