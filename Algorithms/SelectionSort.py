def selection_sort(lst):
    """Selection sort, if the dataset is big, Time complexity is O(n^2) (in worst, best and average cases),
    The Best-case: O(n^2), best case occurs when the array is already sorted.
    Average-case: O(n^2), the average case arises when the elements of the array are in a disordered or random order, without a clear ascending or descending pattern.
    The worst-case scenario arises when we need to sort an array in ascending order, but the array is initially in descending order.
    Space Complexity: O(1), as no extra space is required for the Selection sort algorithm"""
    for i in range(len(lst)):
        min_index=i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
               min_index=j

        #swap
        lst[i],lst[min_index]=lst[min_index],lst[i]   

    return lst


if __name__=="__main__":
    #lst=[8, 9,10,45,87,2,3,4,5,7]
    #lst=[3,2,7,5]
    lst=[-8, 9,-10,45,87,2,3,4,-5,7]
    sorted= selection_sort(lst)
    print(sorted)