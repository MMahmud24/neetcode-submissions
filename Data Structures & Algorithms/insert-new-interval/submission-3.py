class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        newIntervals = []

        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            newIntervals.append(intervals[i])
            i+=1
        
        while i < n and not (newInterval[1] < intervals[i][0]):
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i+=1

        newIntervals.append(newInterval)

        while i < n:
            newIntervals.append(intervals[i])
            i+=1

        return newIntervals