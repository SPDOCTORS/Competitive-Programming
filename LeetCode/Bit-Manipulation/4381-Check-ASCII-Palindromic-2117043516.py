class Solution:
    def isPalindromic(self, s: str) -> bool:
        bits=[]
        for ch in s:
            bits.append(format(ord(ch),"08b"))
        binary="".join(bits)
        return binary==binary[::-1]
        