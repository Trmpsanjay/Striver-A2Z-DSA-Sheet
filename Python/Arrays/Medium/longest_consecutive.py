from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Longest Consecutive Sequence (LeetCode 128)

        Goal:
        - Given an unsorted array of integers, return the length of the longest
          consecutive elements sequence.
        - Must run in O(n) average time.

        High-level intuition:
        - Convert the list into a set for O(1) average lookups.
        - Only start counting from numbers that are the *start* of a sequence.
          A number `num` is a sequence start if `num - 1` is NOT in the set.
          This avoids re-counting sequences from the middle (duplicate work).

        Layman example:
        - Think of numbers as houses on a street with addresses: 100, 101, 102, ...
        - You only start walking a "consecutive block" from a house if there is
          no house directly before it (address - 1).
        - Then you keep walking forward while the next house exists.

        Real-life analogy:
        - Attendance roll numbers / ticket numbers:
          You want the longest streak of continuous ticket numbers.
          You only begin a streak at a ticket that doesn't have its immediate predecessor.

        Complexity:
        - Building set: O(n)
        - Each number is effectively visited at most once as part of a sequence extension
          (because we only start from sequence starts).
        - Overall average time: O(n)
        - Space: O(n) for the set

        Common pain points / mistakes:
        1) Not checking for "start of sequence":
           - If you start from every number, you repeatedly count the same streak, leading to O(n^2).
        2) Using list membership checks instead of set:
           - `x in nums` is O(n); must use a set for O(1) average.
        3) Forgetting edge case: empty input -> should return 0.
           - This code handles it naturally because num_set becomes empty and max_count stays 0.
        4) Inner loop bounds:
           - You used `range(num+1, num + 3 + len(num_set))` as a safe upper bound.
             It works, but a `while` loop is usually cleaner.
        """
        # Convert to set for O(1) average membership checks
        num_set = set(nums)

        max_count = 0

        # Iterate over unique numbers
        for num in num_set:
            # Start counting only if num is the beginning of a sequence
            if num - 1 not in num_set:
                count = 1

                # Try to extend the sequence forward: num+1, num+2, ...
                # The upper bound here is just a "safe limit" to avoid infinite looping;
                # the loop breaks as soon as the streak ends.
                for i in range(num + 1, num + 3 + len(num_set)):
                    if i in num_set:
                        count += 1
                    else:
                        # streak broke, update max and stop extending this start
                        max_count = max(count, max_count)
                        break

        return max_count
