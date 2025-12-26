class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Dutch National Flag Algorithm (3-way partition)

        Layman + real-life intuition:
        Imagine you have a line of balls in 3 colors:
          0 = Red, 1 = White, 2 = Blue
        and you want them arranged as: Red ... Red, White ... White, Blue ... Blue

        Real-life example:
        Think of a factory conveyor belt where items are labeled:
          0 = "Send to Left bin"
          1 = "Keep in Middle bin"
          2 = "Send to Right bin"

        You maintain 3 regions in the same array:
        1) [0 ... curr-1]      -> all 0s (left bin done)
        2) [curr ... itr-1]    -> all 1s (middle bin done)
        3) [last+1 ... end]    -> all 2s (right bin done)
        And you're scanning the "unknown" region: [itr ... last]

        Pointers meaning:
        - curr: where the next 0 should go (start of the 1s zone)
        - itr : current scanner index (exploring unknown items)
        - last: where the next 2 should go (end boundary)

        What you do while scanning:
        - If you see 0:
            swap it to the front (to curr), because 0 belongs on the left,
            then move both curr and itr forward.
        - If you see 2:
            swap it to the back (to last), because 2 belongs on the right,
            move last backward ONLY (do NOT move itr yet)
            because the element you swapped in from the end is "unknown"
            and must be checked.
        - If you see 1:
            it's already in the correct middle region, just move itr forward.

        Key trick (important):
        - On swapping with last for a 2, we don't increment itr,
          because we haven't processed the swapped-in element yet.
        """

        itr = 0                 # scanner pointer over the array
        curr = 0                # next position to place a 0
        last = len(nums) - 1    # next position to place a 2

        while itr <= last:
            if nums[itr] == 0:
                # Put 0 into the left region
                nums[curr], nums[itr] = nums[itr], nums[curr]
                curr += 1
                itr += 1

            elif nums[itr] == 2:
                # Put 2 into the right region
                nums[itr], nums[last] = nums[last], nums[itr]
                last -= 1
                # itr NOT incremented because swapped element might be 0/1/2 and needs checking

            else:
                # nums[itr] == 1 -> already belongs in the middle region
                itr += 1
