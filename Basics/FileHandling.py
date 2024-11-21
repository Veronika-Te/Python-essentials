#1
def open_file_append_line():
    try:
        myfile=open('append_mode.txt','w')
        myfile.write('Hello text file\n')
        myfile.close()

        myfile=open('append_mode.txt', 'a')
        myfile.write('Goodbye text file') #appended line
        myfile.close()

        myfile=open('append_mode.txt', 'r')
        text =myfile.read()
        myfile.close()
        return text
    except:
       msg="FileExistsError"
       return msg

#2
def open_file_x_mode():
    try:
       myfile2=open('exclusive_mode.txt','x') 
       myfile2.write('Hello! Text file was opened in exclusive mode')
       myfile2.close()
       myfile2=open('exclusive_mode.txt', 'r')
       text=myfile2.read()
       myfile2.close()
       return text
    except:
       msg="FileExistsError"
       return msg

#3
def add_sentence_to_file(text_to_append):
    try:
       myfile3=open('specific_position.txt','w')
       myfile3.write(" Python is useful for accomplishing real-world tasks he sorts of things developers do day in and day out. \n It's commonly used in a variety of domains, as a tool for scripting other components and implementing \n standalone programs. ")
       myfile3.close()
       myfile3=open('specific_position.txt','r')
       text_1=myfile3.read()
       myfile3.close()

       myfile3=open('specific_position.txt','r+')
       myfile3.seek(0,2)
       myfile3.write(text_to_append)
       myfile3.close()
       myfile3=open('specific_position.txt','r')
       text=myfile3.read()
       myfile3.close()
       return text_1, text
    except:
        msg="FileExistsError"
        return msg
#4
def find_duplicates_in_text():
    myfile4=open('Rabbit.txt','r')
    lines=myfile4.read().splitlines()
    check_words=set()
    check_words=("example","all","word", "up" , "did ", "him")
    dict_words={}
    for line in lines:
        tokens=line.split(" ")
        for item in tokens:
            litem = item.lower()
            if(litem in check_words):
                if (litem in dict_words):
                    dict_words[litem]+=1
                else:
                    dict_words[litem]=1
    return dict_words
        
if __name__=="__main__":
 res=open_file_append_line()
 print(f"append_mode.txt:\n{res} ")

 res2=open_file_x_mode()
 print(f"exclusive_mode.txt: {res2}")


 text_to_append = "In fact, as a general-purpose language. Python's roles are virtually unlimited: \n you can use it for everything from website development and gaming to robotics and spacecraft control."
 res3=add_sentence_to_file(text_to_append)
 print("------Text in file------")
 print(f"{res3[0]} \n")
 print("------After adding sentence to the end position-------")
 print(f"{res3[1]}")
 print("________________________________")
 res_dict=find_duplicates_in_text()
 print("Words count:")
 for key,value in res_dict.items():
     print(key,value)
