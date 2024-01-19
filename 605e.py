class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # 1. Iterate through flowerbed
        # 2. If a flower can be planted, subtract 1 from n; else, ignore the next element if it's a 0

        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                flowerbed[0] = 1
                n -= 1

        for i in range(0, len(flowerbed)):
            # Edge case of idx being the first element
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            # Edge case of idx being the last element
            elif i == len(flowerbed) - 1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            # Valid to check one before and one after
            elif i - 1 > 0 and i + 1 < len(flowerbed) - 1:
                if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1

        # n should be less than or equal to 0 if it works
        if n <= 0:
            return True

        return False

        