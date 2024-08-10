def read_file_count_characters(file_name:str)->int:
    """Opens the text file in read mode and counts characters in it"""
    try:
       file=open(file_name,'r')
       text=file.read()
       if not text:
          return 0
       splitted=text.split()
       if not splitted:
          return 0
       #Counts charachters in string 
       count=0
       for i in splitted:
           count+=len(i)
       return count
    except:
       raise IOError
    #TODO change exception handling
    finally:   
       file.close()

def read_file_count_words(file_name:str)->int:
    """Opens the text file in read mode and counts words in it"""
    try:
       file=open(file_name,'r')
       text=file.read()
       if not text:
          return 0
       splitted=text.split()
       if not splitted:
          return 0
       #Words count 
       return len(splitted)
    finally: 
       file.close()    

def read_file_count_lines(file_name:str)->int:
    """Opens the text file in read mode and counts lines in it"""
    try:
       file=open(file_name,'r')
       lines=file.read().splitlines()
       if not lines:
          return 0
       count_lines=len(lines) 
       return count_lines
    finally: 
       file.close()   
       
def analysing_text(file_name:str)->tuple:
    """Gets results of text analysis"""
    char_count=read_file_count_characters(file_name) 
    words_count= read_file_count_words(file_name)    
    lines_count=read_file_count_lines(file_name)
    return char_count,words_count,lines_count

def write_analysing_text(file_name:str)->None:
    """Writes results of analysis into text file"""
    res=analysing_text(file_name)
    str1=f"Count of characters in text: {res[0]}\nCount of words in text: {res[1]}\nCount of lines in text: {res[2]}\n"
    try:
       newfile=open("Text analysis.txt","w")
       newfile.write(str1)
    finally:
       newfile.close()
        
def main()->None:
    try: 
       file_name="The Tale of Peter Rabbitt.txt"
       write_analysing_text(file_name)
    except IOError as e:
      print("Failed. File not found")
 

if __name__=="__main__": 
    main()
 
    