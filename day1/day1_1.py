frequency = 0
with open("input.txt") as fp:
    for line in fp:
        change = int(line)
        frequency += change
print(frequency)