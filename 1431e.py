class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = 0
        res = []

        for candy in candies:
            if candy > maxCandy:
                maxCandy = candy

        for candy in candies:
            if candy + extraCandies >= maxCandy:
                res.append(True)
            else:
                res.append(False)

        return res
        