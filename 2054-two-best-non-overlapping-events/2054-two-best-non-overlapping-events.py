class Solution:
    def maxTwoEvents(self, events):
        # Sort events by end time
        events.sort(key=lambda x: x[1])
        
        n = len(events)
        ends = [events[i][1] for i in range(n)]
        
        # best[i] = maximum value from events[0..i]
        best = [0] * n
        best[0] = events[0][2]
        for i in range(1, n):
            best[i] = max(best[i - 1], events[i][2])
        
        ans = 0
        
        for i in range(n):
            start, end, value = events[i]
            
            # Binary search for last event ending before start-1
            left, right = 0, i - 1
            idx = -1
            while left <= right:
                mid = (left + right) // 2
                if ends[mid] < start:
                    idx = mid
                    left = mid + 1
                else:
                    right = mid - 1
            
            # Take this event alone
            ans = max(ans, value)
            
            # Take this event + best previous non-overlapping event
            if idx != -1:
                ans = max(ans, value + best[idx])
        
        return ans