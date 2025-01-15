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
            if d == "" or d == ".":
                continue
            elif d == ".." and len(ret) > 0:
                ret.pop()
            elif d != "..":
                ret.append(d)

        s = "/" + "/".join(ret)
        return s if s != "" else "/"
        