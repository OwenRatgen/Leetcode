class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        elif len(t) == 0:
            return False

        trail = 0
        for head in range(0, len(t)):
            if s[trail] == t[head]:
                trail += 1
            
            if trail == len(s):
                return True

        return False
        