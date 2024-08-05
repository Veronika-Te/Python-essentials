def count_words(text:str)->int:
    """Counts words in string"""
    if not text:
       return 0
    splitted=text.split()
    if not splitted:
       return 0
    return len(splitted)

def count_characters(text:str)->int:
    """Counts charachters in string"""
    if not text:
       return 0
    splitted=text.split()
    if not splitted:
       return 0
    count=0
    for i in splitted:
        count+=len(i)
    return count

def isWordinText (text:str, **words:str)->bool:
    """Checks if word is in text"""
    if not text or not words:
       return False
    word=words['word1']
    if word in text:
       return True
    return False 
   
       
def replace_word(text:str, **words:str)->str:    
    """Replaces word in text"""
    if not text or not words:
       return False
    #if word1.isalpha() and word2.isalpha():
    word1=words['word1']
    word2=words['word2']
    if word1 in text:
       #replaced=text.replace(word1,word2,1) #first occurence
       replaced=text.replace(word1,word2)
    return replaced       

def get_keys(dictionary):
    if not dictionary: 
       return
    return set(dictionary.keys())

def process_text(text:str, operation:str, **kwargs):
    """Uses this dictionary to perform the requested text processing operation."""
    
    text_operations={'Count words': count_words, 'Count characters': count_characters, 'If word in text': isWordinText , 'Replace word': replace_word}
    keys_set = get_keys(text_operations)

    if not text or not operation and not kwargs: 
       return "Parameters are missing"
     
    if operation in keys_set:
       if operation=='Count words':
          countwrds=text_operations.get(operation)
          count=countwrds(text)
          return count
       elif operation=='Count characters':
          countchars=text_operations.get(operation)
          chars=countchars(text)
          return chars
       elif operation=='If word in text':
          check=text_operations.get(operation)
          check_b=check(text,**kwargs)
          return check_b
       elif operation=='Replace word':
          replace=text_operations.get(operation)
          replaced_txt=replace(text,word1="continuously",word2="constantly")
          return replaced_txt
       else:
          return "Invalid operation"
    return "Invalid operation"
    
def main():
  
  text="Yerevan is the capital and largest city of Armenia, as well as one of the world's oldest continuously inhabited cities."
  print("________Initial text________")
  print(text)
  print("\n")
  
  #Count words
  operation1='Count words'
  res1=process_text(text, operation1)
  print("Count of words:", res1)
  print("\n") 
  
  #Count characters
  operation2='Count characters'
  res2=process_text(text, operation2)
  print("Count of characters:", res2)
  print("\n")
  
  #Checking existence of word in text
  operation3='If word in text'
  first_word='is'
  
  res3=process_text(text, operation3, word1=first_word)
   
  if res3:
     print(f"Yes. Word: '{first_word}', exists in text ")
  else: 
     print(f"No. Word: '{first_word}', is missing")
  print("\n")
  
  #Replacing
  first_word= "continuously"
  result_word="constantly"
  operation4='Replace word'
  res4=process_text(text, operation4, word1=first_word, word2=result_word)
  print("________Replaced_________")
  print(res4)

if __name__=="__main__":
  main()