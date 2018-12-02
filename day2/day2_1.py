two = 0
three = 0
with open("input.txt") as fp:
    for line in fp:
        bucket = {}
        line = line.rstrip()
        for c in line:
            if not bucket.get(c):
                bucket[c] = 1
            else:
                bucket[c] += 1
        values = bucket.values()
        if 2 in values:
            two += 1
        if 3 in values:
            three += 1
checksum = two * three
print(checksum)