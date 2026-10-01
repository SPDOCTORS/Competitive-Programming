class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_pos=[-1]*3
        total=0
        for po in range(len(s)):
            last_pos[ord(s[po])-ord("a")]=po

            total += 1 + min(last_pos)
        return total

            
        