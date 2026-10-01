class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = dict(knowledge)
        ans = []
        end = -1

        for i, ch in enumerate(s):
            if i <= end:
                continue

            if ch == "(":
                end = s.find(")", i)
                key = s[i + 1:end]

                if key in d:
                    ans.append(d[key])
                else:
                    ans.append("?")
            else:
                ans.append(ch)

        return "".join(ans)
        