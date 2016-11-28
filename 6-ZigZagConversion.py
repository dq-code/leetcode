__author__ = 'qianden'
class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        out_list = []
        for i in range(numRows):
            out_list.append([])
        cur_col = 0
        cur_row = 0
        for item in list(s):
            cur_row = 0 if cur_row == numRows else cur_row
            mod = cur_col%(numRows-1)
            if mod == 0:
                out_list[cur_row].append(item)
                cur_row += 1
                if cur_row == numRows:
                    cur_col += 1
            else:
                out_list[numRows-1-mod].append(item)
                cur_col += 1

        out_str = ""
        for l in out_list:
            out_str += ''.join(l)
        return out_str

if __name__ == "__main__":
    input_str = "PAYPALISHIRING"
    row = 3
    runner =Solution()
    print runner.convert(input_str, row)



