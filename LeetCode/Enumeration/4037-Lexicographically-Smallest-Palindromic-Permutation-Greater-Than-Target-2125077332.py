class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n=len(s)
        freq=[0]*26
        for ch in s:
            freq[ord(ch)-ord('a')]+=1
        middle=""
        odd=0
        for i in range(26):
            if freq[i]%2==1:
                odd+=1
                middle+=chr(ord('a')+i)
        if odd!=n%2:
            return ""
        half_freq=[0]*26
        for i in range(26):
            half_freq[i]=freq[i]//2
        m=n//2
        left=[]
        i=0
        while i<m:
            idx=ord(target[i])-ord('a')
            if half_freq[idx]>0:
                left.append(target[i])
                half_freq[idx]-=1
                i+=1
            else:
                break
        if i<m:
            idx = ord(target[i]) - ord('a')
            for j in range(idx + 1, 26):
                if half_freq[j] > 0:
                    left.append(chr(ord('a') + j))
                    half_freq[j] -= 1
                    for k in range(26):
                        left.extend(
                            [chr(ord('a') + k)] * half_freq[k]
                        )
                    left = "".join(left)
                    return left + middle + left[::-1]
        if i == m:
            current_left = "".join(left)
            result = current_left + middle + current_left[::-1]
            if result>target:
                return result
                
        for pos in range(len(left) - 1, -1, -1):
            old_idx = ord(left[pos]) - ord('a')
            half_freq[old_idx] += 1
            for j in range(old_idx + 1, 26):
                if half_freq[j] > 0:
                    new_left = left[:pos]
                    new_left.append(chr(ord('a') + j))
                    half_freq[j] -= 1
                    for k in range(26):
                        new_left.extend(
                            [chr(ord('a') + k)] * half_freq[k]
                            )
                    new_left = "".join(new_left)
                    result = new_left + middle + new_left[::-1]
                    if result > target:
                        return result
                    half_freq[j] += 1
        return ""

