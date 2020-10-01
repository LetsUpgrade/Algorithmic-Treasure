 ## DOCUMENTATION

 ## All the algorithms are coded in Python Language
## First Repeatng Element 
<img src="https://img.shields.io/badge/-Amazon-blue" height="25">&nbsp;&nbsp;<img src= "https://img.shields.io/badge/-Oracle-green" height="25">&nbsp;&nbsp;<br>
### Problem Statement
  An array arr[] of size N is given . <br>
  Find the first repeating element in an array of integers,i.e.,an element that occurs more than once and whose index of first occurrence is smallest.<br>
           
           Sample :
           Input: [1,2,3,4,3,1,6]  
           Output: element: 3 ; index: 2
     
  ## Solution : <br>
  ## Optimized Approach:- <br>
   The program is solved using function <br>
   **first_repeating** function is declared with two arguments( arr : a array which stores  the elements , n: size of the array) <br>
    the whole logic behind the program is that : <br>
    **Min** is initialized to its minimum value (-1) <br>
    a dictionary is declared <br>
    a loop will transverse through the array from right to left  <br>
    if the element is  present in the dictionary then <br>
    update the **Min** <br>
    and if the element is not present ,then add the element in the dictionary<br>
    print the element with its index number.<br>
    
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
