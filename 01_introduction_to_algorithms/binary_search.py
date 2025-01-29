def binary_search(arr, item):
    lower_idx = 0
    higher_idx = len(arr)
    while(lower_idx <= higher_idx):
        idx = (lower_idx + higher_idx) // 2
        if arr[idx] == item:
            print(f"Item Found At Index: {idx}")
            break;
        elif arr[idx] > item:
            higher_idx = idx - 1
        else:
            lower_idx = idx + 1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
item = 4

binary_search(arr, item)
