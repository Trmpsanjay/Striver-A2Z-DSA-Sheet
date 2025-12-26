class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer–Moore Voting Algorithm
        #
        # Intuition (think of it like an election):
        # - We keep a "current candidate" (majority) and a "vote count" (count).
        # - When we see the same number as the candidate, it gets a vote (+1).
        # - When we see a different number, it cancels out a vote (-1).
        # - If votes drop to 0, it means the candidate has been fully "canceled out"
        #   by different numbers seen so far, so we pick a new candidate from the next number.
        #
        # Why this works:
        # - The true majority element appears more than n/2 times, so it cannot be fully canceled.
        # - After all cancellations, the remaining candidate must be the majority element.

        majority = nums[0]   # start by assuming the first element is the candidate
        count = 1            # it starts with one vote

        for i in range(1, len(nums)):
            if nums[i] == majority:
                # same as candidate -> candidate gains a vote
                count += 1
            elif count == 0:
                # votes are 0 -> previous candidate got canceled out
                # choose a new candidate and reset votes
                majority = nums[i]
                count = 1
            else:
                # different from candidate -> cancel one vote
                count -= 1

        # print(type(majority))  # debug: majority will be int
        return majority
