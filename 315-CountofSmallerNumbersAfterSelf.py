class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        smaller = [0 for i in range(len(nums))]

        def sort(enum):
            mid = len(enum) / 2
            if mid:
                left = sort(enum[:mid])
                right = sort(enum[mid:])
                for i in range(len(enum) - 1, -1, -1):
                    if (not right and left) or (right and left and left[-1][1] > right[-1][1]):
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum

        sort(list(enumerate(nums)))

        return smaller