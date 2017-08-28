class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if len(nums) == 0: return []

        majorityMap = {}
        for i in range(len(nums)):
            if nums[i] not in majorityMap:
                if len(majorityMap) < 2:
                    majorityMap[nums[i]] = 1
                else:
                    for key in majorityMap.keys():
                        tempvalue = majorityMap[key] - 1
                        if tempvalue == 0:
                            majorityMap.pop(key)
                        else:
                            majorityMap[key] = tempvalue

            else:
                majorityMap[nums[i]] += 1

        res = []
        for key, value in majorityMap.items():
            if value > 0:
                actualCount = 0
                for i in range(len(nums)):
                    if nums[i] == key:
                        actualCount += 1
                if actualCount > len(nums) / 3:
                    res.append(key)

        return res

