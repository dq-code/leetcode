#!/usr/bin/python

import math

class MedianofTwoSortedArray:
    def findMedian(self, arr1, arr2):
        if len(arr1) == 0 and len(arr2) == 0:
            return 0
        if len(arr1) == 0:
            mid = math.floor((len(arr2)-1)/2)
            return arr2[mid]
        if len(arr2) == 0:
            mid = math.floor((len(arr1)-1)/2)
            return arr1[mid]
        num = math.ceil((len(arr1)+len(arr2)/2)         
        if len(arr1)<=len(arr2):
            pos=helper(arr1, arr2, num, 0, len(arr1)-1)
            if pos != -1 :
                return arr1[pos]
            else:
                return arr2[helper(arr2, arr1, num, 0, len(arr2)-1)]
        else:
            pos=helper(arr2, arr1, num, 0, len(arr2)-1)
            if(pos != -1):
                return arr2[pos]
            else:
                return arr1[helper(arr1, arr2, num, 0, len(arr1)-1)]
            
    def helper(self, targetArr, searchArr, num, start, end):
        if start >= end:
            return -1
        mid = math.floor((end-start)/2)+start
        remainNum = num - (mid + 1) 
        if searchArr[remainNum-1] <= targetArr[mid] and searchArr[remainNum+1] >= targetArr[mid]:
            return mid
        else if searchArr[remainNum-1] >= targetArr[mid]:
            mid = helper(arr1, arr2, num, mid + 1, end)
        else if searchArr[remainNum+1] <= targetArr[mid]:
            mid = helper(arr1, arr2, num, start, mid - 1)
        return mid

if __name__ == "__main__":
    caller = MedianofTwoSortedArray()
    arr1 = [1,2,4,5]
    arr2 = [1,3,6,9,10]
    print str(caller.findMedian(arr1, arr2))