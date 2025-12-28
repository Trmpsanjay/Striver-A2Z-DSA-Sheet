from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Transform nums into the next lexicographically greater permutation (in-place).
        If no next permutation exists (array is in descending order), rearrange to the
        smallest permutation (ascending order).

        Lexicographic meaning (layman):
        - Like counting with digits.
          Example: 1 2 3 -> 1 3 2 -> 2 1 3 -> ...
        - "Next permutation" means the next bigger arrangement, with the *smallest* possible increase.

        Real-life analogy:
        - Think of a combination lock where you want the next valid combination.
        - You try to increase the number as little as possible:
          change the rightmost part first, and only touch earlier digits if you must.

        Steps (core intuition):
        1) Find the "pivot" from the right:
           - Move from the end until you find a spot where nums[i-1] < nums[i].
           - nums[i-1] is the pivot: it's the first place where we can make the number bigger.
           - Everything to the right of pivot (suffix) is non-increasing (descending-like).

        2) If no pivot found (array fully non-increasing):
           - It's already the largest permutation.
           - Next permutation is the smallest -> reverse the whole array.

        3) Find the rightmost element in the suffix that is just bigger than the pivot.
           - Swap it with the pivot.
           - Why rightmost? Because the suffix is decreasing, so the first bigger from the end
             is the smallest element that is still > pivot (minimal increase).

        4) Reverse the suffix (nums[i:]) to make it the smallest possible order (ascending).
           - After swap, the suffix is still in decreasing order; reversing makes it increasing.
           - This ensures we get the immediate "next" permutation, not a bigger jump.

        Time Complexity: O(n)
        Space Complexity: O(1) extra (reversal in-place)

        Common pain points / mistakes:
        - Using > instead of >= when finding pivot: duplicates require >=.
        - Forgetting to reverse the suffix after swap (you won't get the next, just "a" bigger one).
        - Picking the wrong swap element: must be the smallest element > pivot (rightmost in suffix).
        """

        # 1) Find pivot index (i-1) such that nums[i-1] < nums[i]
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        # If i == 0, array is fully non-increasing => largest permutation
        if i == 0:
            nums.reverse()
            return

        pivot = i - 1

        # 2) Find rightmost element > pivot to swap with
        j = len(nums) - 1
        while j >= i and nums[j] <= nums[pivot]:
            j -= 1

        # 3) Swap pivot with that element (minimal increase)
        nums[pivot], nums[j] = nums[j], nums[pivot]

        # 4) Reverse suffix to get the smallest arrangement after pivot
        nums[i:] = reversed(nums[i:])
