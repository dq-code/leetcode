class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        nums = sorted(nums, key=int)
        res = []
        store_map={}
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                sum = nums[i]+nums[j]
                if not store_map.has_key(sum):
                    store_map[sum] = []
                store_map[sum].append([i,j])

        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                sub_target = target - nums[i] - nums[j]
                if store_map.has_key(sub_target):
                    for pair in store_map[sub_target]:
                        if pair[0] in range(j+1,len(nums)) and pair[1] in range(j+1, len(nums)):
                            l = [nums[i], nums[j], nums[pair[0]], nums[pair[1]]]
                            if res.count(l) == 0:
                                res.append(l)

        return res

if __name__ == "__main__":
    input = [-5,-4,-3,-2,-1,0,0,1,2,3,4]
    target = 0
    runner =Solution()
    print runner.fourSum(input, target)
