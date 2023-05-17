class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        a=0
        n=len(nums1)+len(nums2)
        for i in range(int(n/2)):
            if nums1==[]:
                a=nums2.pop(0)
            elif nums2==[]:
                a=nums1.pop(0)
            elif nums1[0]<nums2[0]:
                a=nums1.pop(0)
            else:
                a=nums2.pop(0)
        if nums1==[] and nums2==[]:
            k=a
        elif nums1==[]:
            k=nums2.pop(0)
        elif nums2==[]:
            k=nums1.pop(0)
        elif nums1[0]<nums2[0]:
            k=nums1.pop(0)
        else:
            k=nums2.pop(0)
        if n%2==0:
            return (a+k)/2
        else:
            return k
        
        
