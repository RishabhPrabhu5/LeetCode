class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        dirs = path.split("/")
        ret = []
        if len(dirs) == 0:
            return "/"
        for d in dirs:
            if d != ".." and d!= "." and d != "":
                ret.append(d)
            elif d == ".." and len(ret) > 0:
                ret.pop()

        s = ""
        for p in ret:
            if p != "":
                s+= "/" + p
        return s if s != "" else "/"
        