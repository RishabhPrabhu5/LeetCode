class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        i=0
        while i < m+n and j<n:
            if nums1[i]>nums2[j] or i-j >= m:
                nums1.insert(i,nums2[j])
                nums1.pop()
                j +=1
            i+=1
