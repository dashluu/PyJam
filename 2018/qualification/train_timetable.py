# Sort the trip by start times and store them in L
# let S = empty, ta = 0, tb = 0
# for each trip t in L:
#   flag = false
#   for each train r in S:
#       if t starts at A and r.stop == A and r.endtime + turnaround <= t.starttime
#           r.endtime = t.endtime
#           r.stop = B
#           flag = true
#       else if t starts at B and r.stop == B and r.endtime + turnaround <= t.starttime:
#           r.endtime = t.endtime
#           r.stop = A
#           flag = true
#   if flag == false:
#       r = new train
#       S = S U {r}
#       if t starts at A:
#           r.endtime = t.endtime
#           r.stop = B
#           ta += 1
#       else if t starts at B:
#           r.endtime = t.endtime
#           r.stop = A
#           tb += 1
# return ta, tb

class Trip:
    def __init__(self, start_loc, start_time, end_time) -> None:
        self.start_loc = start_loc
        self.start_time = start_time
        self.end_time = end_time

class Train:
    def __init__(self) -> None:
        self.stop = None
        self.end_time = 0

def str_to_time(str):
    line = str.split(':')
    return int(line[0]) * 60 + int(line[1])

def read_test():
    turnaround = int(input())
    line = input().split()
    na = int(line[0])
    nb = int(line[1])
    trips = []
    for j in range(na):
        line = input().split()
        start_time = str_to_time(line[0])
        end_time = str_to_time(line[1])
        trips.append(Trip('A', start_time, end_time))
    for j in range(nb):
        line = input().split()
        start_time = str_to_time(line[0])
        end_time = str_to_time(line[1])
        trips.append(Trip('B', start_time, end_time))
    return trips, turnaround

def solve_test(trips, turnaround):
    trips = sorted(trips, key=lambda x: x.start_time)
    trains = []
    ta = 0
    tb = 0
    for t in trips:
        flag = False
        for r in trains:
            if t.start_loc == 'A' and r.stop == 'A' and r.end_time + turnaround <= t.start_time:
                r.end_time = t.end_time
                r.stop = 'B'
                flag = True
                break
            elif t.start_loc == 'B' and r.stop == 'B' and r.end_time + turnaround <= t.start_time:
                r.end_time = t.end_time
                r.stop = 'A'
                flag = True
                break
        if not flag:
            r = Train()
            trains.append(r)
            if t.start_loc == 'A':
                r.end_time = t.end_time
                r.stop = 'B'
                ta += 1
            else:
                r.end_time = t.end_time
                r.stop = 'A'
                tb += 1
    return ta, tb

def solve():
    ntest = int(input())
    for i in range(ntest):
        trips, turnaround = read_test()
        ta, tb = solve_test(trips, turnaround)
        print("Case #{}: {} {}".format(i + 1, ta, tb))

solve()
