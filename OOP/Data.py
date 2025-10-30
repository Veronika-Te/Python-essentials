# with PUBLIC field
class PublicData:
  def __init__(self, data):
      self.data = data  

# with PRIVATE field
class PrivateData:
  def __init__(self, data):
    self.__data = data  

  # Getter
  def get_data(self):
    return self.__data

  # Setter with validation
  def set_data(self, new_data):
    if isinstance(new_data, str) and new_data.strip():
      self.__data = new_data
    else:
      print("❌ Invalid data. Must be a non-empty string.")



if __name__=="__main__":
  print("🔹 PublicData Example:")
  public = PublicData("Valid info")
  print("Initial:", public.data)

  # Anyone can modify public data (even to invalid)
  public.data = None
  print("Modified to invalid:", public.data)

  print("\n🔹 PrivateData Example:")
  private = PrivateData("Secret info")
  print("Initial:", private.get_data())

  # Trying to modify directly — fails
  try:
    private.__data = None
  except AttributeError as e:
    print("Error:", e)

  # Correct way — through setter
  private.set_data("")
  private.set_data("Updated info")
  print("After valid update:", private.get_data())

  # Direct access fails:
  print("Direct access attempt:", getattr(private, "__data", "❌ Not accessible"))
