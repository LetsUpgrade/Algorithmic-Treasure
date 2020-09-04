 ## DOCUMENTATION
 
## All the algorithms are coded in Python Language
## Sort an array of 0s, 1s and 2s
<img src="https://img.shields.io/badge/-Amazon-yellow" height="30">&nbsp;&nbsp;


### Problem Statement
Given two sorted arrays arr[] and brr[] of size N and M respectively.<br>
Find the union of these two arrays.



       Sample :
       Input: M=7 arr1 = [1,2,2,4,5,5,6] 
       Input: N=7 arr2 = [6,6,7,7,8,9,9]
       Output: {1,2,4,5,6,7,8,9}
 
 ## Solution : <br>
  ## Optimized Approach:- <br>
 (i) Accept elements in the array **arr[] and brr[]**  and store their lenght in two separate variable.<br>
 (ii) Merge the two array using **"+"** operator and store it in a variable .<br>
         (iii) sort the merged array using **"sorted()"** function  <br>
         (iv) store the sorted merged array in set [Since set does not contain duplicate elements ]  <br>
         (v)  return the final array.
    
  ## Time and Space complexity  <br>
 Time Complexity :- O(m+n)<br>
         Space Complexity:- O(m+n)
  
  ##  Pseudocode <br>
  def function(arr1, arr2 , M ,N):<br>
            result = arr1 + arr2 <br>
           return sorted(set(result))  <br>  
