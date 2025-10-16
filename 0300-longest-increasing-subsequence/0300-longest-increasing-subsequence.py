class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = 1
        storage = [(nums[-1], 1)]
        for i in range(len(nums)-2, -1, -1):
            # print(nums[i], storage)
            found = False
            best = 1
            place = 0
            max_idx = 0
            for j in range(len(storage)):
                if storage[j][0] > nums[i]:
                    val = storage[j][1]+1
                    # print("found")
                    if not found:
                        place = j
                    found = True
                    if val > best:
                        best = val
                        max_idx = j
                        if best > max_val:
                            max_val = best
                    


            if not found:
                storage = storage + [(nums[i], 1)]
            else:
                # print(max_idx, max_val)
                storage = storage[:place] + [(nums[i], storage[max_idx][1]+1)] + storage[place:]
                
        return max_val

        