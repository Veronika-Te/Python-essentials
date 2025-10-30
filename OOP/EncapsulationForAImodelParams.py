class AIModel:
  def __init__(self, learning_rate):
    self.__learning_rate=None
    self.set_learning_rate(learning_rate)
    
  def get_learning_rate(self):
    return self.__learning_rate
  
  def set_learning_rate(self, value):
    if 0 < value<=1:
      self.__learning_rate=value
    else:
      print("Invalid learning rate")
      
if __name__=="__main__":
  model = AIModel(0.05)
  print("✅ Initial learning rate:", model.get_learning_rate())

  # Try invalid value
  model.set_learning_rate(2.5)
  print("After invalid attempt:", model.get_learning_rate())

  # Try valid value
  model.set_learning_rate(0.8)
  print("✅ Updated learning rate:", model.get_learning_rate())

  # Direct modification is impossible
  print("Direct access attempt:", getattr(model, "__learning_rate", "❌ Not accessible"))