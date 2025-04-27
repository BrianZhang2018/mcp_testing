def two_sum(nums, target):
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    
    Args:
        nums (List[int]): Array of integers
        target (int): Target sum
        
    Returns:
        List[int]: Indices of the two numbers that add up to target
    """
    # Create a dictionary to store numbers we've seen and their indices
    seen = {}
    
    # Loop through the array with index
    for i, num in enumerate(nums):
        # Calculate the complement (what we need to find)
        complement = target - num
        
        # If we've seen the complement before, return the indices
        if complement in seen:
            return [seen[complement], i]
            
        # Otherwise, add the current number and its index to our dictionary
        seen[num] = i
    
    # If no solution is found
    return None

# Example usage
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")
    print(f"Explanation: Because nums[{result[0]}] + nums[{result[1]}] == {target}")