class Solution:
    def checkValidString(self, s: str) -> bool:
        opencount=0
        closecount=0
        length=len(s)-1

        for i in range(len(s)):
            if s[i]=="(" or s[i]=="*":
                opencount+=1
            else:
                opencount-=1
            if s[length-i]==')' or s[length-i]=="*":
                closecount+=1
            else:
                closecount-=1
            if opencount<0 or closecount<0:
                return False
        return True
        
        