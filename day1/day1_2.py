frequency = 0
array = []
seen = set()

with open("input.txt") as fp:
    for line in fp:
        change = int(line)
        array.append(change)

match = False
while True:
    for x in array:
        frequency += x
        if frequency in seen:
            match = True
            break
        seen.add(frequency)
    if match:
        break

print(frequency)
