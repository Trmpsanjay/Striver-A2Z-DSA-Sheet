from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merge overlapping intervals.

        Approach 1 (commented below): Two-pointer "in-place" idea
        - Sort intervals.
        - Use i for the current interval, j for the next interval.
        - If overlap (end of i >= start of j), extend intervals[i][1] and pop j.
        - Else move both pointers forward.
        Note: In Python, pop(j) is O(n) due to shifting, so worst-case can become O(n^2).

        Approach 2 (active / optimal): Build a merged result list
        - Sort intervals.
        - Scan left to right and maintain a 'merged' list.
        - If current interval doesn't overlap with the last merged interval, append it.
        - Otherwise extend the last merged interval's end.
        Complexity: O(n log n) time (sorting dominates) and O(n) extra space.

        Args:
            intervals: List of [start, end] intervals (may be unsorted).

        Returns:
            A list of merged, non-overlapping intervals sorted by start time.
        """

        # -----------------------------
        # Approach 1: two pointers (mutates intervals)
        # -----------------------------
        # intervals.sort()                       # sort by start time
        # i = 0                                  # points to current interval to merge into
        # j = 1                                  # points to next interval to compare
        # while j < len(intervals):
        #     end_num_lst1 = intervals[i][-1]     # end of current interval (intervals[i][1])
        #     start_num_lst2 = intervals[j][0]    # start of next interval
        #
        #     # If current interval overlaps (or touches) the next one
        #     if end_num_lst1 >= start_num_lst2:
        #         # Extend current interval's end to cover the next interval's end
        #         intervals[i][1] = max(intervals[i][1], intervals[j][1])
        #
        #         # Remove the merged interval at j
        #         # IMPORTANT: do NOT increment j here because elements shift left,
        #         # and a new interval is now at index j that we must compare again.
        #         intervals.pop(j)
        #
        #     else:
        #         # No overlap: move to the next pair
        #         i += 1
        #         j += 1
        #
        # return intervals

        # -----------------------------
        # Approach 2: optimal (build merged list)
        # -----------------------------
        intervals.sort()                  # ensure intervals processed in increasing start order
        merged: List[List[int]] = []      # output list of merged intervals

        for s, e in intervals:            # s=start, e=end of the current interval
            # If merged is empty OR current interval starts after last merged ends => no overlap
            if not merged or merged[-1][1] < s:
                merged.append([s, e])     # start a new merged block
            else:
                # Overlap: extend the last merged interval end if needed
                merged[-1][1] = max(merged[-1][1], e)

        return merged
