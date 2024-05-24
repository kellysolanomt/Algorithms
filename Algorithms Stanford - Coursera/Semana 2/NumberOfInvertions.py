def sort_count_split_inv(array):
    n = len(array)
    if n <= 1:
        return array, 0
    A, Ac = sort_count_split_inv(array[:n//2])
    B, Bc = sort_count_split_inv(array[n//2:])
    count = 0 + Ac + Bc
    i = 0
    j = 0
    C = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
            count += len(A) - i
    if i < len(A):
        C.extend(A[i:])
    if j < len(B):
        C.extend(B[j:])
        
    return C, count


array = []
with open('Algorithms\Algorithms Stanford - Coursera\Semana 2\IntegerArray.txt', 'r') as f:
    for line in f:
        array.append(int(line.strip()))

print(f"Number of invertions: {sort_count_split_inv(array)[1]}")

