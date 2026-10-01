class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_s=0
        digit_prod=1
        sumi=0
        ori=n
        while n>0:
            digit=n%10
            n=n//10
            digit_s+=digit
            digit_prod*=digit
        return ori%(digit_s+digit_prod)==0

        