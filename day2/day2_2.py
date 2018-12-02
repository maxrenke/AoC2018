with open("input.txt") as fp:
    bucket = {}
    for line in fp:
        line = line.rstrip()
        i = 0
        for c in line:
            sub = line[:i] + line[i+1:]
            if not bucket.get(i):
                bucket[i] = [sub]
            else:
                bucket[i] += [sub]
            i += 1
    for i in bucket:
        lst = bucket[i]
        seen = set()
        match = [x for x in lst if lst.count(x) > 1]
        if match:
            print(match[0]) 