import statistics
def find_mean(lst):
    """Calculates mean """
    if not lst:
       return 0
    l=len(lst) 
    get_sum = sum(lst) 
    mean = get_sum / l
    return mean
 
def find_median(lst):
    """Calculates median """
    if not lst:
       return 0
    length=len(lst) 
    lst.sort()
    if length % 2 == 0:  #if length is even
       median1 = lst[length//2] 
       median2 = lst[length//2 - 1] 
       median = (median1 + median2)/2
       return median
    else: 
       median = lst[length//2] 
       return median
       
def find_mode(lst):
    """Calculates mode"""
    if not lst:
       return 0
    return statistics.mode(lst) 

def find_standart_deviation(lst):
    """calculates the standard deviation"""
    if not lst:
       return 0
    return statistics.pstdev(lst)


lst= [1, 2, 3, 4, 5] 
def analyze_data(data, operation):
    """ Performs statistical analysis on a list of numbers."""
    
    analyze_tool={'Mean':find_mean,'Median':find_median,'Mode':find_mode,'SD':find_standart_deviation}

    if not data or not operation:
       return 0
    operations={"Mean","Median","Mode","SD"} 
    if (isinstance(data, (list))):
        if operation in operations:
            if operation=="Mean":
               mean=analyze_tool.get(operation)
               return mean(data)
            elif operation=="Median":
               median=analyze_tool.get(operation)
               return median(data) 
            elif operation=="Mode":
               mode=analyze_tool.get(operation)
               return mode(data)  
            elif operation=="SD":
               sd=analyze_tool.get(operation)
               return sd(data) 
            else:
               return 0
        else:
           return 0
    else:
       return 0
    
def main():  
     print("Statistics")
     #lst= [1, -2, -3,-3, -4, -5,5,5,-5,5]
     lst= [1,2,3,4,4,5,8,8,8,8]
     print(lst)
     #Mean
     mean=analyze_data(lst, "Mean")
     print(f"Mean : {mean}")
     #Median
     median=analyze_data(lst, "Median")
     print(f"Median : {median}")
     #Mode
     mode=analyze_data(lst, "Mode")
     print(f"Mode : {mode}")
     #Standart Deviation
     sd=analyze_data(lst, "SD")
     print(f"SD: {sd}")
     
if __name__=="__main__":
   main()

 
    
