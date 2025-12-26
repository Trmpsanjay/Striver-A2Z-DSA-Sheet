from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        """
        Rearrange Array Elements by Sign (alternate + and -)

        Problem expectation (typical LeetCode version):
        - nums contains equal number of positive and negative integers
          (often: positives > 0, negatives < 0; sometimes 0 is treated as positive in solutions)
        - Return an array where:
            index 0 -> positive
            index 1 -> negative
            index 2 -> positive
            index 3 -> negative
            ... and so on

        Key idea (intuition):
        - Build a new answer array (in-place is not feasible here without extra trickery,
          because we need stable alternating placement).
        - Keep two pointers:
            pos_index = 0 (next even position for a positive)
            neg_index = 1 (next odd position for a negative)
        - Scan nums once and place each number into its correct slot.

        Layman example:
        Imagine arranging people in a line:
        - Even seats (0,2,4,...) are reserved for "Team A" (positives)
        - Odd seats  (1,3,5,...) are reserved for "Team B" (negatives)
        As you meet each person, you send them directly to their next reserved seat.

        Real-life example:
        Event seating with alternating badges:
        - Green badge must sit on even chairs, Red badge on odd chairs.
        - You keep two "next available chair" counters and fill them as people arrive.

        Time Complexity: O(n)
        Space Complexity: O(n) because we create `ans`

        Common pain points / mistakes:
        1) Constraints mismatch:
           - If positives and negatives are NOT equal, this approach can run out of bounds.
           - This solution assumes counts are balanced (as in the common problem statement).

        2) Handling zero:
           - This code treats 0 as positive (`num >= 0`).
           - If the problem defines 0 differently, adjust the condition.

        3) Index increments:
           - Must do `+= 2` so positives only go to even indices and negatives to odd indices.
        """
        pos_index = 0  # next even index to place a non-negative / positive number
        neg_index = 1  # next odd index to place a negative number

        ans = [0] * len(nums)  # output array

        for num in nums:
            if num >= 0:
                # Place positive (or zero) at the next even slot
                ans[pos_index] = num
                pos_index += 2
            else:
                # Place negative at the next odd slot
                ans[neg_index] = num
                neg_index += 2

        return ans
