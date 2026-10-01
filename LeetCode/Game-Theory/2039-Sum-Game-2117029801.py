class Solution:
    def sumGame(self, num: str) -> bool:
        leftq=0
        rightq=0
        n=len(num)
        left_s=0
        right_s=0
        for i in range(n):
            if i<n//2:
                if num[i]=="?":
                    leftq+=1
                else:
                    left_s+=int(num[i])
            else:
                if num[i]=="?":
                    rightq+=1
                else:
                    right_s+=int(num[i])
        if leftq==rightq:
            return left_s!=right_s
        if (leftq+rightq)%2==1:
            return True
        left_final = left_s + (leftq // 2) * 9
        right_final = right_s + (rightq // 2) * 9
        return left_final != right_final
            
        