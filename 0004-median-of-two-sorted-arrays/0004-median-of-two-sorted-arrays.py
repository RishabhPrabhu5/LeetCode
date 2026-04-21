class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2
        
        # Always binary search the smaller array
        if len(A) > len(B):
            A, B = B, A
        
        total = len(A) + len(B)
        half = total // 2
        
        l, r = 0, len(A)
        
        while l <= r:
            i = (l + r) // 2      # partition in A
            j = half - i          # partition in B
            
            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < len(A) else float("inf")
            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < len(B) else float("inf")
            
            # correct partition
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:  # odd
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
       



        