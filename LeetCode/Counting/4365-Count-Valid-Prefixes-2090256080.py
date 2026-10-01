class Solution:
    def countValidPrefixes(self, s: str) -> int:
        zero=0
        one=0
        cnt=0
        for ch in s:
            if ch=='0':
                zero+=1
            else:
                one+=1
            if abs(zero-one)<=1:
                cnt+=1
        return cnt
        
                
            
                
        