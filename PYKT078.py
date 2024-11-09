t = int(input())

while t != 0:
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    am = [x for x in a if x < 0]
    duong = [x for x in a if x >= 0]
    maxA = max(duong)

    idx = duong.index(maxA)
    duong.insert(idx, m)
    print(*am, *duong)

    t -= 1