from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Return the maximum possible sum of a non-empty contiguous subarray.

        This uses Kadane's Algorithm.

        Core idea (intuition):
        - At each index, decide:
            1) Extend the previous subarray by adding nums[i]
               OR
            2) Start a brand-new subarray at nums[i]
        - Track the best sum seen so far.

        Why your version failed on [-1]:
        - You initialized max_sum = 0, which incorrectly allows the "empty subarray" (sum 0).
        - But the problem requires a *non-empty* subarray, so for all-negative arrays,
          the answer must be the largest (least negative) element.

        Example:
            nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
            Output = 6  (subarray [4, -1, 2, 1])

        Time Complexity:
            O(n)  (single pass)
        Space Complexity:
            O(1)  (constant extra space)
        """
        # Initialize with the first element to correctly handle all-negative arrays.
        curr_sum = nums[0]  # best subarray sum that MUST end at current position
        max_sum = nums[0]   # best subarray sum seen anywhere so far

        for x in nums[1:]:
            # Either extend the previous streak or start fresh at x
            curr_sum = max(x, curr_sum + x)

            # Update global best
            max_sum = max(max_sum, curr_sum)

        return max_sum
