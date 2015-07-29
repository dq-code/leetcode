__author__ = 'qianden'
class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        BASE = 10
        remain = abs(x)
        sign = -1 if x<0 else 1
        output = 0
        while remain is not 0:
            output = output*BASE+remain%BASE
            remain = int(remain/BASE)
        if output > 2147483647:
            return 0
        return sign*output

if __name__ == "__main__":
    input = -123
    runner =Solution()
    print runner.reverse(input)



