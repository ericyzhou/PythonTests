# Longest increasing subsequence
def find_sequence(arr):
    list_of_seq = []

    for x in arr:
        if len(list_of_seq) == 0:
            list_of_seq.append([x])
        else:
            for seq in list_of_seq:
                if len(seq) == 1:
                    if seq[0] < x:
                        seq.append(x)
                    else:
                        seq[0] = x
                elif x < seq[0]:
                    list_of_seq.append([x])
                else:
                    if seq[len(seq) - 1] < x:
                        seq.append(x)
                    elif seq[len(seq) - 1] > x > seq[len(seq) - 2]:
                        seq[len(seq) - 1] = x
                    else:
                        pass
    return get_longest(list_of_seq)


def get_longest(arr):
    best_length = 0
    best_seq = []
    for x in arr:
        if len(x) > best_length:
            best_length = len(x)
            best_seq = x
    return best_seq


a = [23, 24, 25, 15, 16, 17, 18, 19, 0, 20,
     21, 100, 22, 23, 24, 25, 1, 2, 3, 4, 5, 6]
b = find_sequence(a)

for x in b:
    print(str(x), end=" ")
