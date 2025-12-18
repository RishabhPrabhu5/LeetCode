class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        buckets = defaultdict(set)
        freq = defaultdict(int)
        for i in range(n):
            freq[nums[i]] +=1

        for num in freq:
            buckets[freq[num]-1].add(num)
        
        idx = n-1
        count = 0
        ret = []
        
        while idx > -1 and count < k:
            if buckets[idx] != set():
                to_add = list(buckets[idx])
                while count < k and len(to_add) > 0:
                    ret.append(to_add.pop())
                    count +=1
            idx -=1
            
        return ret
        