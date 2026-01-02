from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Two Sum (return indices)

        Logic to remember:
        - For each number x, the partner needed is: needed = target - x
        - If we've already seen `needed`, we found the answer.
        - Otherwise store x with its index for future.

        Real-life analogy:
        - Budget = target.
        - While scanning item prices, for each price x you ask:
          "Do I already have an item priced (target - x)?"
          If yes, those two items complete the budget.

        Complexity:
        - Time: O(n) average (hash lookups)
        - Space: O(n)

        Common mistakes:
        - Storing before checking can break when target is 2*x and duplicates matter.
          (Your code checks first, then stores -> correct.)
        """

        map = {}  # number -> index where we saw it

        for i in range(len(nums)):
            nums_to_be_find = target - nums[i]   # needed partner to reach target

            # If partner already seen, return its index + current index
            if map.get(nums_to_be_find) is not None:
                return [map.get(nums_to_be_find), i]

            # Otherwise remember current number for future matches
            else:
                map[nums[i]] = i

        return None
