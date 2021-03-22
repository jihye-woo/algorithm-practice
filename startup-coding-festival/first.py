from datetime import datetime


N = int(input())
starts = []
ends = []
for i in range(N):
    line = input()
    period = line.split(" ~ ")
    start = datetime.strptime(period[0], '%H:%M')
    starts.append(start)
    end = datetime.strptime(period[1], '%H:%M')
    ends.append(end)

final_start = max(starts)
final_end = min(ends)

if(final_end < final_start):
    print("-1")
else:
    print(datetime.strftime(final_start, '%H:%M') + " ~ " + datetime.strftime(final_end, '%H:%M'))



