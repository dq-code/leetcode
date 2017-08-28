class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = 1 if numerator*denominator>=0 else -1
        numerator = abs(numerator)
        denominator = abs(denominator)
        nums = []
        loop_dict = {}
        cnt = 0
        loop_str = ""
        while True:
            nums.append(str(numerator/denominator))
            cnt+=1
            numerator = (numerator%denominator)*10
            if numerator==0:
                break
            if numerator in loop_dict:
                loop_str = "".join(nums[loop_dict[numerator]:cnt])
                break
            loop_dict[numerator] = cnt
        res = nums[0]
        if len(nums)>1:
            res += "."
        if loop_str:
            res+="".join(nums[1:]).replace(loop_str, "")+"("+loop_str+")"
        else:
            res+="".join(nums[1:])

        if sign<0:
            res = "-"+res

        return res

