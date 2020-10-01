 ## DOCUMENTATION

 ## All the algorithms are coded in Python Language
## Quick Sort On Linked List 
<img src="https://img.shields.io/badge/-Paytm-green" height="30">&nbsp;&nbsp;


### Problem Statement

   Sort the given Linked List using Quick Sort. 

   **Input:**
    A method takes 1 argument: address of the head of the linked list. 
    The struct Node has a data part which stores the data and a next pointer which points to the next element of the linked list.
    There are multiple test cases. For each test case, this method will be called individually.

   **Output:**
   Set *link to head of resultant linked list.

           
           Sample :
         Input: [10 -> 7 -> 11-> 12-> 6]   
          Output:[ 6 -> 7 -> 10-> 11-> 12]  
     
  ## Solution : <br>
  ## Optimized Approach:- <br>
  a temporary variable **Pivot** will store the element of the very first node  <br>
  Traverse the loop through the list and store the values to the **left side**  of the pivot value which are less than pivot <br>
  and store the values to the **right side** of the pivot value which are greater than pivot   <br>
  Now the value of pivot is located to it desired position  <br>
  Store the value of the pivot  <br>
  Now, sort the elements before the pivot value and after the pivot value in the same manner as done before by calling the functions. <br>
  Finally print the sorted list  
  
    
  ## Time and Space complexity  <br>
  Time Complexity : O(n^2) [Worst Case]<br>
                    O(n log n) [ Average case]<br>
  Space Complexity : O(1) <br>
  ##  Pseudocode <br>
  
partition(a,lb,il)<br>
           Pivot =a[lb] <br>
           i=lb <br>
           j= ub <br>
           while (i<j): <br>
             while(a[i] <=Pivot ) : <br>
                i++ <br>
             while(a[j]> pivot  ):<br>
                 j--   <br>  <br>
             Swap (a[i],a[j])
            Swap(a[pivot],a[j])
            return end
            
   QuickSort(a,lb,ub)<br>
            if (lb<ub)<br>
             loc = Partition (a,lb,ub)<br>
          QuickSort(a,lb,loc-1)<br>
          QuickSort(a,loc+1,ub)<br>
