class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        hmap1 = defaultdict(int)
        for n1 in nums1:
            for n2 in nums2:
                hmap1[n1+n2] +=1
        
        hmap2 = defaultdict(int)
        for n3 in nums3:
            for n4 in nums4:
                hmap2[n3+n4] +=1
        
        count = 0
        for num in hmap1.keys():
            count += hmap1[num] * hmap2[-1*num]

        return count
        