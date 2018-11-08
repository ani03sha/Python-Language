from datetime import datetime as dt

# Format
frmt = '%a %d %b %Y %H:%M:%S %z'
for _ in range(int(input())):
    t1 = dt.strptime(input(), frmt)
    t2 = dt.strptime(input(), frmt)
    print(int(abs((t1 - t2).total_seconds())))
