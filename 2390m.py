class Solution:
    def removeStars(self, s: str) -> str:
        res = ""
        stack = [*s]
        num_stars = 0

        while stack != []:
            curr_letter = stack.pop()
            if curr_letter == "*":
                num_stars += 1
            else:
                if num_stars == 0:
                    res += curr_letter
                else:
                    num_stars -= 1

        return res[::-1]