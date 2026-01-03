from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge Sorted Array (LeetCode 88)

        Goal:
        - nums1 has length m+n, with first m elements valid and last n as extra space (0s).
        - nums2 has n elements.
        - Merge nums2 into nums1 in sorted order IN-PLACE.

        Simple memory trick:
        ✅ "Fill from the back"
        Because the end of nums1 has empty space, so we can safely place the largest elements there.

        Pointers:
        - i = last valid element in nums1 (m-1)
        - j = last element in nums2 (n-1)
        - k = last position in nums1 (m+n-1) where we should write next

        Real-life analogy:
        - Two sorted stacks of papers (smallest on top, largest at bottom).
        - You want to build one final sorted stack from the bottom (largest first),
          so you always pick the larger bottom paper and place it at the end.

        Complexity:
        - Time: O(m+n)
        - Space: O(1)

        Common pain points:
        1) Merging from front overwrites nums1 values -> that's why we go from back.
        2) Forgetting remaining nums2 elements:
           - If nums1 finishes early, nums2 leftovers must be copied.
        3) Copying remaining nums1 elements is optional:
           - They are already in correct place, but your code copies them (still correct).
        """

        # since both are sorted here start from last point
        # and take pointer to be filled at last of first array and start filling from the last
        k = m + n - 1  # write pointer (last index of nums1)
        i = m - 1      # last valid index in nums1
        j = n - 1      # last index in nums2

        # compare from the back and place bigger element at nums1[k]
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                # nums1 element is bigger -> place it at the end
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            else:
                # nums2 element is bigger/equal -> place it at the end
                nums1[k] = nums2[j]
                j -= 1
                k -= 1

        # now if any element is remaining from i or j fill them
        # (leftover nums1 part is already sorted, copying it is fine but not required)
        while i >= 0:
            nums1[k] = nums1[i]
            k -= 1
            i -= 1

        # leftover nums2 must be copied (important case)
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
