class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        r = "".join(reversed(s))

        for i in range(len(s) // 2):
            if s[i] == r[i]:
                continue
            else:
                return False
        return True
