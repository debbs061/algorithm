class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        resLen = 0

        for i in range(len(s)):  # for every i, consider it as a center of the palindrome.
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r + 1 - l > resLen:
                    resLen = r + 1 - l
                    res = s[l:r + 1]
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r + 1 - l > resLen:
                    resLen = r + 1 - l
                    res = s[l:r + 1]
                l -= 1
                r += 1
        return res
