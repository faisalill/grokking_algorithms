def binary_search(arr, item):
    lower_idx = 0
    higher_idx = len(arr)
    idx = (higher_idx - lower_idx)  // 2
    while(arr[idx] != item):
        idx = (higher_idx - lower_idx)  // 2
        if arr[idx] > item:
            higher_idx = idx - 1
        else:
            lower_idx = idx + 1
    print(f"Item Found At Index: {idx}")

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
item = 3

binary_search(arr, item)

