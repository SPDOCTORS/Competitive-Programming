class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        length = [0] * (n + 1)
        for i, ch in enumerate(s):
            cur = length[i]
            if 'a' <= ch <= 'z':
                length[i + 1] = cur + 1
            elif ch == '*':
                length[i + 1] = max(0, cur - 1)
            elif ch == '#':
                length[i + 1] = cur * 2
            elif ch=='%':
                length[i + 1] = cur

        final_len = length[n]
        if k < 0 or k >= final_len:
            return '.'
        for i in range(n - 1, -1, -1):
            ch = s[i]
            before = length[i]
            after = length[i + 1]
            if 'a' <= ch <= 'z':
                if k == before:
                    return ch
            elif ch == '*':
                pass
            elif ch == '#':
                if k >= before:
                    k -= before

            else: 
                k = before - 1 - k

        return '.'

        