class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x:x[0])

        res = [intervals[0]]

        for current in intervals[1:]:
            prev = res[-1]

            if prev[1] >= current[0]:
                prev[1] = max(prev[1],current[1])
            else:
                res.append(current)
        
        return res

        
        