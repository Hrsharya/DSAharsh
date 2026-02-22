def find_peak(arr):
    n = len(arr)
    for i in range(n):
        # Check left and right neighbors
        left_ok = (i == 0 or arr[i] >= arr[i-1])
        right_ok = (i == n-1 or arr[i] >= arr[i+1])
        
        if left_ok and right_ok:
            return arr[i]