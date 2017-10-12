class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        move_map = {'R':[1,0], 'L':[-1,0], 'U':[0,1], 'D':[0,-1]}
        start = [0,0]
        for m in moves:
            start[0] += move_map[m][0]
            start[1] += move_map[m][1]
        return start[0]==0 and start[1]==0