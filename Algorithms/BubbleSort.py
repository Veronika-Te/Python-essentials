def bubble_sort(lst):
    """Bubble Sort, if our dataset is small or partially sorted we can use this algorithm.
    Worst-case scenario, the outer(first) loop runs O(n) times. As a result, the worst-case time complexity of bubble sort is O(n x n) = O(n^2).
    Best-case scenario, the array is already sorted, but just in case, bubble sort performs O(n) comparisons,as a result - O(n).
    Average Case : Bubble sort may require (n/2) passes and O(n) comparisons for each pass in the average case. Time complexity of bubble sort is O(n/2 x n) = O (n2)."""
    n=len(lst)
    for i in range(n):
        #if it possible to terminate sorting earlier(in order to optimize)
        already_sorted=True
        for j in range(n-i-1):
            if lst[j]>lst[j+1]:
                #swap
                lst[j], lst[j+1]=lst[j+1],lst[j]
                #print(lst)
                
                #in order to continue loop
                already_sorted=False
         
        #if in the end there is no pair to swap, it means that sorting ended
        if already_sorted:
            break
        
    return lst
        



if __name__=="__main__":
    #lst=[8, 9,10,45,87,2,3,4,5,7]
    #lst=[3,2,7,5]
    lst=[-8, 9,-10,45,87,2,3,4,-5,7]
    sorted= bubble_sort(lst)
    print(sorted)