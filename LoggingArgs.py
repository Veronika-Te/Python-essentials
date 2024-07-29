import logging

def handle_list_of_messages(*args)->None: 
    """Prints message, date, time according to level of severity"""
    if not args:
       return 
    for i in args:
        severity=i[2]
        if severity.upper():
           if severity=="DEBUG":
              print(f" Severity: {severity}, Message: '{i[3]}', Date: {i[0]}, Time: {i[1]}")
           elif severity=="INFO":
              print(f" Severity: {severity}, Message: '{i[3]}', Date: {i[0]}, Time: {i[1]}")
           elif severity=="WARNING":
              print(f" Severity: {severity}, Message: '{i[3]}', Date: {i[0]}, Time: {i[1]}")
           elif severity=="ERROR":
              print(f" Severity: {severity}, Message: '{i[3]}', Date: {i[0]}, Time: {i[1]}")
           elif severity=="CRITICAL":
              print(f" Severity: {severity}, Message: '{i[3]}', Date: {i[0]}, Time: {i[1]}")
           else:
              print("Message with unknown severity")
        else:
           print("Unknown severity")
    

def handle_metadata_of_logs(**kwargs)->None:
    """Prints data of log message"""
    if not kwargs:
        return 0
    #print(kwargs)
    for k,v in kwargs.items():
        print(k,v)

def main()->None:
    # logging.basicConfig(level=logging.DEBUG,
    #                     format="%(asctime)s %(levelname)s %(message)s",
    #                     datefmt="%Y-%m-%d %H:%M:%S",)
    #                     #filename="basic.log")    if we add filename, info would be stored in other file
    # logging.debug("This is a debug message.")
    # logging.info("This is an info message.")
    # logging.warning("This is a warning message.")
    # logging.error("This is an error message. ")
    # logging.critical("This is a critical message.")


    #Result   
    ls1=["2024-07-26", "16:38:08", "DEBUG", "This is a debug message."]
    ls2=["2024-07-26", "16:38:08","INFO","This is an info message."]
    ls3=["2024-07-26", "16:38:08","WARNING","This is a warning message."]
    ls4=["2024-07-26", "16:38:08","ERROR","This is an error message."]
    ls5=["2024-07-26", "16:38:08","CRITICAL","This is a critical message."]
 
    
    handle_list_of_messages(ls1,ls2,ls3,ls4,ls5)
    print("\n")
    handle_metadata_of_logs(ymd='2024-07-26',time='16:38:08',lvl='DEBUG',msg='This is a debug message.')     

if __name__=="__main__":
    main()