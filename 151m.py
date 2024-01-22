class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) == 1:
            return s
        s = s.split()

        left = 0
        right = len(s) - 1

        while left < right:
            copy_left = s[left]
            s[left] = s[right]
            s[right] = copy_left
            left += 1
            right -= 1

        return " ".join(s)

        