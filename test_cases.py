
def nth_largest_number(nums, n):
    if n <= 0 or n > len(nums):
        return "Invalid input: N out of range"
    
    
    sorted_nums = sorted(nums, reverse=True)
    
    
    return sorted_nums[n - 1]


nums = [14, 67, 48, 23, 5, 62]
n = 4


result = nth_largest_number(nums, n)
print(f"{n}th Largest number: {result}")
