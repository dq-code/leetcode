import re


class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        content_map = {}
        for path in paths:
            details = path.split()
            directory = details[0]
            for i in range(1, len(details)):
                match = re.match('(.*)\((.*)\)$', details[i])
                file = match.group(1)
                content = match.group(2)
                content_key = hash(content)
                if content_key not in content_map:
                    content_map[hash(content)] = []
                content_map[hash(content)].append(directory + '/' + file)
        res = []
        for key in content_map.keys():
            if len(content_map[key]) > 1:
                res.append(content_map[key])

        return res
