def find_uniq(arr):
    for i in range(len(arr)): 
        if arr[i] != arr[i+1]: break
    return arr[i+1] if i != 0 else (arr[i] if arr[1] == arr[2] else arr[1])
