class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_even = sum(nums[i] for i in range (0, len(nums), 2))
        total_odd = sum(nums[i] for i in range(1, len(nums), 2))

        pref_even = 0
        pref_odd = 0
        fair_count = 0

        for i, num in enumerate(nums):
            suff_even = total_even - pref_even
            suff_odd = total_odd - pref_odd

            if i % 2 == 0:
                suff_even -= num
            else:
                suff_odd -= num

            new_even_sum = pref_even + suff_odd
            new_odd_sum = pref_odd + suff_even

            if new_even_sum == new_odd_sum:
                fair_count += 1

            if i % 2 == 0:
                pref_even += num
            else:
                pref_odd += num

        return fair_count