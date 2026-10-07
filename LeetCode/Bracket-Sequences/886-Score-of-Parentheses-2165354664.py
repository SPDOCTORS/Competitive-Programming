class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score=0
        balance=0
        for i,c in enumerate(s) :
            if c=="(":
                balance+=1
            else:
                balance-=1
                if s[i-1]=="(":                
                    score+=1<<balance
        return score