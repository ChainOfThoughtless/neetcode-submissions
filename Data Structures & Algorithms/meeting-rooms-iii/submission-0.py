from heapq import heappush, heappop, heapify
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        meeting_counts = [0] * n
        available_rooms = [i for i in range(n)] # order by indices
        busy_rooms = [] # order by end_time, room_idx

        for start, end in meetings:
            # busy -> free
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room_idx = heappop(busy_rooms)
                heappush(available_rooms, room_idx)

            # pick available
            if not available_rooms:
                end_time,  room_idx = heappop(busy_rooms)
                end = end_time + (end - start)
                heappush(available_rooms, room_idx)
            
            # add to busy
            room_idx = heappop(available_rooms)
            heappush(busy_rooms, (end, room_idx))
            meeting_counts[room_idx] += 1

        #return max idx of the room with max meeting count
        return meeting_counts.index(max(meeting_counts))