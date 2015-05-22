class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        map={}
        for i in range(len(nums)):
            rt = nums[i]
            target_index = map.get(target-rt)
            if target_index:
                return [target_index, i+1]
            else:
                map[rt]=i+1       
