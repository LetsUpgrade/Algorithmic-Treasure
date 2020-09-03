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
   **remove_duplicate** function is declared with two arguments( arr : a array which stores  the elements , n: size of the array) <br>
    the whole logic behind the program is that : <br>
    a loop will transverse through the array <br>
    if the current element  is not equal to the next element of the array then , store the element in a temporary list  <br>
    store the temporary assigned list to the original array and print the unique elements
  ## Time and Space complexity  <br>
    Time Complexity :- O(n)<br>
         Space Complexity:- O(1)
  ##  Pseudocode <br>
   y=0          <br>
   for x in 0...len(arr): <br>
   if(arr[x] !=arr[y]: <br>
   arr[x] = arr[y]; <br>
   x++              <br>
   return x+1  
         
