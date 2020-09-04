 ## DOCUMENTATION

 ## All the algorithms are coded in Python Language
## Anagram  
<img src="https://img.shields.io/badge/-Nagarro-green" height="30">&nbsp;&nbsp;


### Problem Statement

  Two strings a and b consisting of lowercase characters are given.<br>
  Check whether two given strings are an anagram of each other or not. <br>
  **Note8** : An anagram of a string is another string that contains the same characters, only the order of characters can be different. <br>

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
  Now, sort the elements before the pivot value  and after the pivot value in the same manner as done before by calling the functions. <br>
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
