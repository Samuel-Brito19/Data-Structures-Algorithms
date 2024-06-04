class Solution(object):
    def isSubsequence(self, s, t):
        i, j = 0, 0
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        if i == len(s):
            return True
        return False
