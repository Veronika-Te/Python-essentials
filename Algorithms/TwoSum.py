def twoSum(nums, target):
  seen = {}  
  for i, num in enumerate(nums):
    diff = target - num  
    if diff in seen:   
      return [seen[diff], i]
    seen[num] = i  
  return None

if __name__=="__main__":
  nums = [3,2,4]
  target = 6
  res=twoSum(nums, target)
  print(res)