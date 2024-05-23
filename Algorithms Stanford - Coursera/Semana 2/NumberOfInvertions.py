array = []
with open('/IntegerArray.txt', 'r') as f:
    for line in f:
        array.append(int(line))
print(array)