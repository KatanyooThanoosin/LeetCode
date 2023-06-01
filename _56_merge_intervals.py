class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        l=[intervals[0]]
        for i in range(1,len(intervals)):
            if l[-1][1]>=intervals[i][0]:
                l[-1][1]=max(l[-1][1],intervals[i][1])
            else:
                l.append(intervals[i])
        return l
