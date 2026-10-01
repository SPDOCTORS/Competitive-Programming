class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        n='123456789'
        l=[]
        for i in range(0,9):
            for j in range(i+1,10):
                num=int(n[i:j])
                if low<=num<=high:
                    l.append(num)
        l.sort()
        return l
            

                

        