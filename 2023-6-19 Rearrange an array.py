# short and simple solution

def arrange(arr, n):
    new = arr.copy()
    for i in range(n):
        arr[i] = new[new[i]]
    return arr