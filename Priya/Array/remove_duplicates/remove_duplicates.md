## DOCUMENTATION

## All the algorithms are coded in Python Language
## First Repeatng Element 
<img src="https://img.shields.io/badge/-Morgan Stanley-purple" height="30">&nbsp;&nbsp;
<img src= "https://img.shields.io/badge/-Samsung-green" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-Wipro-yellow" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-Xome-blue" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-Zoho-red" height="30">&nbsp;&nbsp;<br>
### Problem Statement
   A sorted array **arr**of size **n**. T
    Print the new array **arr[]** with no duplicate element.<br>
           
           Sample :
          Input: [1,2,2,4,5,5,6] 
          Output: [1,2,4,5,6]
     
  ## Solution : <br>
  ## Optimized Approach:- <br>
  the program is solved using function <br>
    remove_duplicate function is declared with two arguments( arr : a array which stores  the elements , n: size of the array) <br>
    the whole logic behind the program is that : <br>
    a loop will transverse through the array <br>
    if the current element  is not equal to the next element of the array then , store the element in a temporary list  <br>
    store the temporary assigned list to the original array and print the unique elements
  ## Time and Space complexity  <br>
   Time Complexity: O(n)  <br>
   Space Comlexity:O(1)  <br>
  ##  Pseudocode <br>
   Min =-1 <br>
   newset=dict()   <br>
   for x in n-1..-1..-1:  <br>
   if arr[x] in newset.keys():   <br>
   Min = x   <br>
   else:   <br>
   myset[arr[x]] = 1   <br>
   print(arr[min], min)  <br>
