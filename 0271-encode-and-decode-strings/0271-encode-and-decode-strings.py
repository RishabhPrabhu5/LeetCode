class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        ret = ""
        for s in strs:
            ret += str(len(s))
            ret+= "#"
            ret += s
        return ret
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        ret = []
        index = 0
        while index < len(s)-1:
            num = ""
            offset = 0
            while s[index + offset] != "#":
                num+=s[index+offset]
                offset +=1
            ret.append(s[index+offset+1: index+offset + int(num)+1])
            index += offset + int(num) + 1
        return ret
        

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))