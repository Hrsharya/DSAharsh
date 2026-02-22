def max_subarray_sum(arr):
    max_so_far = arr[0]
    current_max = arr[0]
    
    for i in range(1, len(arr)):
        # Decide: extend existing subarray or start new one?
        current_max = max(arr[i], current_max + arr[i])
        # Update global maximum
        max_so_far = max(max_so_far, current_max)
        
    return max_so_far