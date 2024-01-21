class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) - 1
        vowels = "aeiouAEIOU"
        s = [*s]

        while left < right:
            if s[left] not in vowels:
                left += 1
            if s[right] not in vowels:
                right -= 1
            if s[left] in vowels and s[right] in vowels:
                copy_left = s[left]
                s[left] = s[right]
                s[right] = copy_left
                left += 1
                right -= 1
                
        return "".join(s)

        