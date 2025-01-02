import queue

for _ in range(int(input())):
    n = int(input())
    q = queue.Queue()
    q.put('2')
    q.put('4')
    q.put('6')
    q.put('8')
    while q.empty() == False:
        top = q.get()
        x = top +top[::-1]
        if int(x) >= n:
            break
        print(x, end=' ')
        q.put(top + '0')
        q.put(top + '2')
        q.put(top + '4')
        q.put(top + '6')
        q.put(top + '8')
    print('')