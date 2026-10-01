class Solution:
    def count(self,string:str,value:str)->int:
        cnt=0
        for ch in string:
            if ch==value:
                cnt+=1
        return cnt
    def transformStr(self, s: str, strs: List[str]) -> List[bool]:
        n=len(s)
        zero_s=self.count(s,'0')
        one_s=self.count(s,'1')
        res=[]
        for string in strs:
            zero_string=self.count(string,'0')
            one_string=self.count(string,'1')
            diff_0=zero_s-zero_string
            diff_1=one_s-one_string
            if diff_0<0 or diff_1<0:
                res.append(False)
                continue
            string=list(string)
            for i in range(n):
                if diff_0==0:
                    break
                if string[i]=='?':
                    string[i]='0'
                    diff_0-=1
            for i in range(n):
                if diff_1==0:
                    break
                if string[i]=='?':
                    string[i]='1'
                    diff_1-=1
            s_oneindex=0
            str_oneindex=0
            solved=True
            for i in range(n):
                if s[i]=='1':
                    s_oneindex+=1
                if string[i]=='1':
                    str_oneindex+=1
                if str_oneindex>s_oneindex:
                    solved=False
                    break
            res.append(solved)
        return res
            
            
            


        