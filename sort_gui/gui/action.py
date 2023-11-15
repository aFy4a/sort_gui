def sort(arr):
    temp = ""
    for i in range(len(arr)):
        if arr[i] < 6:
            temp += str(arr[i]) + ' '

    return temp