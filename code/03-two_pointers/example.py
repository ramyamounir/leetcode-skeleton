
def twoSum(numbers, target):
  # Initialize two pointers
  left = 0
  right = len(numbers) - 1

  # Loop until the pointers meet
  while left < right:

    # Check if the sum of the elements at the pointers is equal to the target
    if numbers[left] + numbers[right] == target:
      # Return the indices of the elements
      return [left + 1, right + 1]

    # If the sum is greater than the target, move the right pointer
    # towards the left to decrease the sum
    elif numbers[left] + numbers[right] > target:
      right -= 1

    # If the sum is less than the target, move the left pointer
    # towards the right to increase the sum
    else:
      left += 1

  # Return an empty list if no such elements are found
  return []

# Example usage
print(twoSum([2, 7, 11, 15], 9))  # Output: [1, 2]
