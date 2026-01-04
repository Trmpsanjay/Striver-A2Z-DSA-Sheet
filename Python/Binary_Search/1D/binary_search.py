from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary Search (works only on sorted array in increasing order)

        Idea (intuition):
        - Keep two pointers: si (start) and ei (end)
        - Look at mid:
          * if nums[mid] == target -> found
          * if nums[mid] > target  -> target must be in left half -> move ei
          * if nums[mid] < target  -> target must be in right half -> move si

        Time:  O(log n)
        Space: O(1)

        Common mistakes:
        - Using this on an unsorted array (won't work)
        - Forgetting to move si/ei (causes infinite loop)
        - Wrong loop condition (use si <= ei for inclusive search range)
        """

        si = 0
        ei = len(nums) - 1

        # empty array case handled automatically because ei = -1 and loop won't run
        while si <= ei:
            # safer mid computation (avoids overflow in other languages)
            mid = si + (ei - si) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                # target can only be on the left side
                ei = mid - 1
            else:
                # target can only be on the right side
                si = mid + 1

        return -1
