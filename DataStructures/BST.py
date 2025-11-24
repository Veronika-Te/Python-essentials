class Node:
  def __init__(self,value):
    self.value=value
    self.left=None
    self.right=None
    
class BinarySearchTree:
  def __init__(self):
    self.root=None
    
  def insert(self,value):
    if not self.root:
      self.root=Node(value)
      return
    
    current=self.root
    while True:
      if value < current.value:
        if current.left:
          current=current.left
        else:
          current.left=Node(value)
      else:
        if current.right:
          current = current.right
        else:
          current.right=Node(value)
          return
        
  def preorder(self,node):
    if node: 
      print(node.value, end=" ")
      self.preorder(node.left)
      self.preorder(node.right)
      
  def inorder(self, node):
    if node:
      self.inorder(node.left)
      print(node.value, end=" ")
      self.inorder(node.right)
  
  def postorder(self, node):
    if node:
      self.postorder(node.left)
      self.postorder(node.right)
      print(node.value, end=" ")
      
  def search(self,value):
    current=self.root
    while current:
      if value==current.value:
        return True
      elif value<current.value:
        current=current.left
      else:
        current=current.right
    return False
    
if __name__=="__main__":
  tree=BinarySearchTree()
  for x in [10,5,20,3,7,15]:
    tree.insert(x)
    
  print("Preoder: ")
  tree.preorder(tree.root)
  
  print("\nInorder: ")
  tree.inorder(tree.root)
  
  print("\nPostorder: ")
  tree.postorder(tree.root)
  
  