from typing import List, Tuple

class Solution:
    def maxSubArray(self, nums: List[int]) -> Tuple[int, int, int]:
        """
        Return the maximum subarray sum *and* the indices of that subarray.

        Output:
            (max_sum, start_index, end_index)   # end_index is inclusive

        Kadane's Algorithm + index tracking:

        Layman / real-life intuition:
        Think of your "current streak" like a running profit streak in a business:
        - Each day you add today's profit/loss to your running streak.
        - If adding today makes the streak worse than just starting fresh today,
          you throw away the old streak and start a new one from today.
        - Keep track of the best streak you've ever seen and where it started/ended.

        Why this handles [-1] correctly:
        - We initialize with nums[0], so we never allow an "empty subarray" of sum 0.
          The subarray must be non-empty.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Best subarray sum ending at current position
        curr_sum = nums[0]
        # Best subarray sum overall
        max_sum = nums[0]

        # Track indices for the best subarray
        best_start = best_end = 0

        # temp_start = where the current running subarray started
        temp_start = 0

        for i in range(1, len(nums)):
            x = nums[i]

            # Decide: extend the current subarray OR start fresh at i
            if x > curr_sum + x:
                curr_sum = x
                temp_start = i  # new subarray starts here
            else:
                curr_sum += x   # extend

            # If we found a better subarray, update best indices
            if curr_sum > max_sum:
                max_sum = curr_sum
                best_start = temp_start
                best_end = i

        return max_sum, best_start, best_end
