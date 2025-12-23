def singleNumber(nums) -> int:
  dict={}
  for i in nums:
    if i not in dict.keys():
      dict[i]=i
    
ls=[1,1,2,2,3]
singleNumber(ls)