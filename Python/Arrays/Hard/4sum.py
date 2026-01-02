from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        4Sum (unique quadruplets)

        Pattern to remember:
        ✅ Sort + fix i + fix j + two pointers (left, right)

        Duplicate rules:
        - Skip duplicate i
        - Skip duplicate j
        - After finding a match, move left/right and skip duplicates for both
        """

        ans = []
        nums.sort()
        n = len(nums)

        for i in range(n - 3):
            # skip duplicate i (same fixed first number)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                # skip duplicate j (same fixed second number)
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]

                    if s == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])

                        # move both pointers inward
                        left += 1
                        right -= 1

                        # skip duplicates for left
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        # skip duplicates for right
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif s > target:
                        # sum too big -> decrease by moving right leftwards
                        right -= 1
                    else:
                        # sum too small -> increase by moving left rightwards
                        left += 1

        return ans
