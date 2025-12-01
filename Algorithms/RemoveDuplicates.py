def remove_duplicates(nums: list[int]) -> int:
  if not nums or not isinstance(nums, list):
    return 0
  write = 1
  for read in range(1, len(nums)):
    if nums[read] != nums[read - 1]:
      nums[write] = nums[read]
      write += 1
  return write

if __name__=="__main__":
  nums = [1, 1, 2, 2, 3]
  print(remove_duplicates(nums))