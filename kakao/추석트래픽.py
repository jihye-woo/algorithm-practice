from datetime import datetime, timedelta
import heapq

def solution(lines):
    answer = 0
    times = []

    for line in reversed(lines):
        end = datetime.strptime(line[:23], '%Y-%m-%d %H:%M:%S.%f')
        runtime = float(line[24:].rstrip('s'))
        times.append((end, runtime))

    running_list = []
    now = datetime.now()
    for end_time, runtime in times:
        start = end_time - timedelta(seconds=runtime) + timedelta(milliseconds=1)
        while running_list:
            heap_key, start_time = running_list[0]
            if end_time > start_time:
                break
            if start_time - end_time >= timedelta(seconds=1):
                heapq.heappop(running_list)
            else:
                break
        heapq.heappush(running_list, (now - start, start))
        answer = max(answer, len(running_list))
    return answer

