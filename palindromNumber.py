import  math

__author__ = 'qianden'
class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x<0:
            return False
        div = 1
        BASE = 10
        remain = x/10
        while remain > 0:
            remain = remain/BASE
            div = div * 10
        if div == 1:
            return True
        remain = x
        while div > 0:
            if div == 1:
                return True
            lead = remain/div
            #print "lead %i"%lead
            tail = remain%BASE
            #print "tail %i"%tail
            if lead != tail:
                return False
            remain = (remain%div - tail)/BASE
            #print "remain %i"%remain
            div = div/100
            #print "num of digit %i"%numofDigit
        return True
