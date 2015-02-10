__author__ = 'Tong'
# Given an array of size n, find the majority element. The majority element is the element that appears
# more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.


class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        threshold = len(num) // 2
        word_frequency = {}
        for each in num:
            if word_frequency.get(each):
                word_frequency[each] += 1
            else:
                word_frequency[each] = 1
            if word_frequency[each] > threshold:
                return each


print(Solution().majorityElement([1]))