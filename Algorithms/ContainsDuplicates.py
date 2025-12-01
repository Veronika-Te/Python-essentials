def containsDuplicate(nums):
  if not nums or not isinstance(nums, list):
    return false
  seen = set()
  for num in nums:
      if num in seen:
        return True
      seen.add(num)
  return False
  
  
if __name__=="__main__":
  nums=[1, 2, 3, 1]
  nums2=[1,2,3]
  print(containsDuplicate(nums))
  print(containsDuplicate(nums2))