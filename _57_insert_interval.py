class Solution:
    def insert(self, intervals, newInterval):
        l=[]
        for i in range(len(intervals)):
            if newInterval[1]<intervals[i][0]:
                l.append(newInterval)
                return l+intervals[i:]
            elif newInterval[0]>intervals[i][1]:l.append(intervals[i])
            else:
                newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
        return l+[newInterval]
