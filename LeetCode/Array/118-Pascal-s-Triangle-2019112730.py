class Solution:
    def generaterow(self, row):
        ans = 1
        ans_r = [1]

        for col in range(1, row):
            ans = ans * (row - col)
            ans = ans // col
            ans_r.append(ans)

        return ans_r

    def generate(self, numRows: int) -> List[List[int]]:
        pas_tri = []

        for row in range(1, numRows + 1):
            pas_tri.append(self.generaterow(row))

        return pas_tri
        

        