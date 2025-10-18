class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        temp = set()
        max_len = 0

        for right in range(len(s)):
            while s[right] in temp:
                temp.remove(s[left])
                left += 1
            temp.add(s[right])
            max_len = max(right - left + 1, max_len)

        return max_len

