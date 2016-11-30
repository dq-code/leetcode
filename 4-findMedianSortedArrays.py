class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        isEven = (len(nums1)+len(nums2))%2 == 0
        half = int(math.ceil(float(len(nums1)+len(nums2))/2))
        if isEven:
            return float(self.getKth(nums1, nums2, half)+self.getKth(nums1,nums2,half+1))/2
        else:
            return self.getKth(nums1, nums2, half)
        
    
    def getKth(self, A, B, k):
        if len(A) > len(B):
            return self.getKth(B, A, k)
        if len(A)==0: 
            return B[k-1]
        if k==1:
            return min(A[0], B[0])
        remainA = min(k/2, len(A))
        remainB = k - remainA
        if A[remainA - 1] > B[remainB-1]:
            return self.getKth(B[remainB:], A, remainA)
        else:
            return self.getKth(A[remainA:], B, remainB)


