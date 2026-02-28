class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        str_num = str(num)
        for i in range(len(str_num)):
            if str_num[i] == "6":
                return int(str_num[:i] + "9" + str_num[i+1:])
        return num
        