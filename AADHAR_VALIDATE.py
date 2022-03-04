d = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 0, 6, 7, 8, 9, 5],
    [2, 3, 4, 0, 1, 7, 8, 9, 5, 6],
    [3, 4, 0, 1, 2, 8, 9, 5, 6, 7],
    [4, 0, 1, 2, 3, 9, 5, 6, 7, 8],
    [5, 9, 8, 7, 6, 0, 4, 3, 2, 1],
    [6, 5, 9, 8, 7, 1, 0, 4, 3, 2],
    [7, 6, 5, 9, 8, 2, 1, 0, 4, 3],
    [8, 7, 6, 5, 9, 3, 2, 1, 0, 4],
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
]

p = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 5, 7, 6, 2, 8, 3, 0, 9, 4],
    [5, 8, 0, 3, 7, 9, 6, 1, 4, 2],
    [8, 9, 1, 6, 0, 4, 3, 5, 2, 7],
    [9, 4, 5, 3, 1, 2, 6, 8, 7, 0],
    [4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
    [2, 7, 9, 3, 8, 0, 6, 4, 1, 5],
    [7, 0, 4, 6, 9, 1, 3, 2, 5, 8]
]

inv = [0, 4, 3, 2, 1, 5, 6, 7, 8, 9]


def reverse(arr):
    arr_inv = arr[::-1]
    return arr_inv


def generateCheckSum(arr):
    c = 0
    inv_arr = reverse(arr)
    for i in range(0, len(inv_arr)):
        c = d[c][p[((i + 1) % 8)][inv_arr[i]]]
    return inv[c]


class AadharValidator:
    def valAadhar(self, uid):
        if len(uid) != 12:
            return "Aadhar is not of 12 digits"
        else:
            for i in uid:
                if i.isalpha():
                    return "No numbers to be present in Aadhar"
                else:
                    uid_list = list(map(int, uid))
                    toCheckChecksum = uid_list.pop()
                    if generateCheckSum(uid_list) == int(toCheckChecksum):
                        return True
                    else:
                        return False
