import heapq


class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        n = len(intervals)
        end_time_queue = []
        heapq.heapify(end_time_queue)
        max_rooms = 0

        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        for start_time, end_time in sorted_intervals:
            if len(end_time_queue) > 0 and start_time >= end_time_queue[0]:
                heapq.heappop(end_time_queue)

            heapq.heappush(end_time_queue, end_time)
            max_rooms = max(max_rooms, len(end_time_queue))

        return max_rooms
