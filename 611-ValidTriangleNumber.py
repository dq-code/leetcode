class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nums = sorted(nums)

        def helper(start, end, target):
            while start <= end:
                mid = (start+end)/2
                if nums[mid] >= target:
                    end = mid - 1
                else:
                    start = mid + 1
            return start

        for i in range(0, len(nums)-2):
            for j in range(i+1, len(nums)-1):
                curSum = nums[i] + nums[j]
                index = helper(j+1, len(nums)-1, curSum)
                res += index - j - 1
        return res


class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nums = sorted(nums)
        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                curSum = nums[i] + nums[j]
                k = len(nums) - 1
                while k > j:
                    if curSum > nums[k]:
                        break
                    k -= 1
                res += k - j

        return res