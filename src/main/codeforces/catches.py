# http://codeforces.com/contest/1260/problem/D
import sys
from bisect import bisect_left


def get_time(pwr, cs, goal):
    length = 0
    cnt = 0
    b,e = None, None
    for l,r,_ in filter(lambda x: x[0] <= x[1] and x[2] > pwr, cs):
        if not (b and e):
            b,e = l,r
            continue
        if l <= e:
            e = max(e, r)
        else:
            cnt += 1
            length += (e - b)
            b,e = l,r
    if b:
        cnt += 1
        length += (e - b)
    return goal + (length + cnt) * 2


def search(cs, goal, time, mn, mx):
    l, r = mn, mx
    while l <= r:
        m = (r + l) // 2
        t = get_time(m, cs, goal)
        if t < time:
            r = m - 1
        else:
            l = m + 1
    return l


def solve(cs, goal, solgers, time):
    solgers.sort()
    mn, mx = solgers[0], solgers[-1]
    cs.sort()
    min_pow = search(cs, goal, time, mn, mx)
    return len(solgers) - bisect_left(solgers, min_pow)


if __name__ == '__main__':
    lines = sys.stdin.readlines()
    m, n, k, t = map(int, lines[0].split())
    aa = list(map(int, lines[1].split()))
    catches = []
    for line in lines[2:]:
        l, r, d = map(int, line.split())
        if l <= r:
            catches.append((l, r, d))
    catches.sort()
    print(solve(catches, n, aa, t))


