from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], k: int) -> int:
        """
        Longest Subarray with sum = k  (works with negatives too)

        Core idea (Prefix Sum + first index map):
        - prefix_sum[i] = sum(nums[0..i])
        - subarray (j+1..i) sum = prefix_sum[i] - prefix_sum[j]
        - want: prefix_sum[i] - prefix_sum[j] = k
          => prefix_sum[j] = prefix_sum[i] - k

        So at each index i:
        1) update prefix_sum
        2) if prefix_sum == k -> best length could be i+1 (0..i)
        3) if (prefix_sum - k) seen before at index j -> subarray (j+1..i) sums to k
           length = i - j
        4) store prefix_sum in map ONLY if it's not present:
           - because we want the earliest index to maximize length

        Layman analogy:
        - Think of tracking your running bank balance each day.
        - If today's balance is X and you want a stretch that sums to k,
          you need some earlier balance (X - k).
        - The earliest time you had (X - k) gives the longest stretch.

        Complexity:
        - Time: O(n)
        - Space: O(n)

        Common pain points / mistakes:
        1) Overwriting prefix_sum index:
           - Must keep the FIRST occurrence, not the latest, to get max length.
        2) Assuming k=0 always:
           - Formula works for any k (including 0).
        3) Only works with positives? (No)
           - This works even with negative numbers (unlike sliding window).
        """

        map = {}         # prefix_sum -> earliest index where it occurred
        pre_sum = 0
        max_length = 0

        for i in range(len(nums)):
            pre_sum += nums[i]  # running prefix sum up to index i

            if pre_sum == k:
                # subarray from index 0..i sums to k
                max_length = i + 1
            else:
                # if we have seen (pre_sum - k) before at index j,
                # then subarray (j+1..i) sums to k
                if map.get(pre_sum - k) is not None:
                    max_length = max(max_length, i - map[pre_sum - k])

            # store earliest index for this prefix_sum (don't overwrite)
            if map.get(pre_sum) is None:
                map[pre_sum] = i

        return max_length
