# REQUIRES O(N) SOLUTION, O(N*K) WON'T WORK

import sys
INT_MIN = -sys.maxsize - 1

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = INT_MIN
        window_sum = 0

        # Got the sum of the first k elements so we can subtract the j-k       element later
        for i in range(0, k):
            window_sum += nums[i]

        j = k
        max_avg = window_sum

        for j in range(k, len(nums)):
            # This will hold the k number of elements property since it always subtracts the first element in the recent subset
            window_sum -= nums[j-k]
            window_sum += nums[j]

            if curr_sum > max_avg:
                max_avg = curr_sum
                
        return max_avg / k
        