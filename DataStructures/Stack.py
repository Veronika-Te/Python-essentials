class Stack:
  def __init__(self):
    self.items=[]
    
  def push(self,item):
    if item is None:
      return
    self.items.append(item)
    
  def pop(self):
    if not self.items:
      return None
    return self.items.pop()
  
  def peek(self):
    if not self.items:
      return None
    return self.items[-1]
  
  def is_empty(self):
    return len(self.items)==0
  
  def __repr__(self):
    return f"Stack({self.items})"
  
  def __str__(self):
    return "<-".join(map(str, reversed(self.items)))
  
if __name__=="__main__":
  s=Stack()
  s.push(1)
  s.push(2)
  s.push(3)
  
  # print(s.pop())
  # print(s.peek())
  # print(s.pop())
  
  print(s)
  