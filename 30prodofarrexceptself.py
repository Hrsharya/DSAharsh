def product_except_self(nums):
    n = len(nums)
    res = [1] * n
    
    # Left pass: calculate prefix products
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    
    # Right pass: multiply by suffix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
        
    return res