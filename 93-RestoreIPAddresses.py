class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def helper(index, ip):
            # print index
            if index >= len(s):
                ip = ip[:-1]
                # print ip
                if len(ip.split('.')) == 4:
                    res.append(ip)
                return

            # if s[index] == '0': return
            helper(index + 1, ip + s[index] + '.')

            if s[index] == '0': return
            if index + 2 <= length:
                helper(index + 2, ip + s[index:index + 2] + '.')

            if index + 3 <= length:
                sub = s[index:index + 3]
                if int(sub) <= 255:
                    helper(index + 3, ip + s[index:index + 3] + '.')

            return

        length = len(s)
        if length > 12 or length < 4: return []
        res = []
        helper(0, '')

        return res
