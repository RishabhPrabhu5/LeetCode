class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        ret = []
        all_words2_map = defaultdict(int)
        for word in words2:
            words2_map = defaultdict(int)
            for l in word:
                words2_map[l]+=1
                if words2_map[l]>all_words2_map[l]:
                    all_words2_map[l] = words2_map[l]

        for word in words1:
            flag = True
            words1_map = defaultdict(int)
            for l in word:
                words1_map[l]+=1
            for l in all_words2_map:
                if all_words2_map[l] > words1_map[l]:
                    flag = False
                    break
            if flag != False:
                ret.append(word)
        return ret
        
    
                
        