class Solution(object):
    def isPalindrome(self, s):
        i = 0
        j = len(s) - 1
        count = 0

        while i < j:
            if s[i] != s[j]:
                count += 1
            if s[i] == s[j] and count <= 1:
                i += 1
                j -= 1
            else:
                return False
            return True
