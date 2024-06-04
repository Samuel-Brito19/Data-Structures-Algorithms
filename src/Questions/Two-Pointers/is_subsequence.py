class Solution(object):
    def isSubsequence(self, s, t):
        count1 = 0
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        for i in range(len(t)):
            if s[count1] == t[i]:
                count1 += 1
            if count1 == len(s):
                return True
        return False
