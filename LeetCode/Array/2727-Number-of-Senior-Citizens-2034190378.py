class Solution:
    def countSeniors(self, details: List[str]) -> int:
        sum=0
        for dim in details:
            if int(dim[11:13])>60:
                sum+=1
        return sum
        