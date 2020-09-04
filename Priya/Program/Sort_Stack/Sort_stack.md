 ## DOCUMENTATION

 ## All the algorithms are coded in Python Language
 ## Sort a Stack 
<img src="https://img.shields.io/badge/-Amazon-red" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-Goldman Sachs-yellow" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-IBM-orange" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-Intuit-blue" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-Kuliza-purple" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-Yahoo-brown" height="30">&nbsp;&nbsp;


### Problem Statement
   A stack is given. Sort the stack such that the top of the stack has the greatest element.
          
        Sample :
        Input:  10 2 45 3 7
        Output: 45 10 7 3 2 
        
  ## Solution : <br>
  ## Optimized Approach:- <br>
  (i) create two stack **( s1 , s2 )** and a temporary variable (temp)<br>
         (ii) the original stack **(s1)** should be greater than 0 <br>
         (iii) assign **temp** to  the top element of the original stack , then push  **temp value**  into the another **stack s2**.<br>
         (iv) Now, again assign **temp** to the next top element of the original stack <br>
         (v) check if the **temp** value is **greater than the s2** <br>
              &nbsp then  **push the temp value** to original stack **s1** <br>
              &nbsp else **push the temp value to **s2** <br>
         (vi) return s2 <br>
    
  ## Time and Space complexity  <br>
  Time Complexity :- O(n*n)<br>
  Space Complexity:- O(1)
  ##  Pseudocode <br>
   Create a original stack(s1) , temporary stack s2, temporary variable (temp). <br>
         While s1 is NOT empty :  <br>
               Assign temp to the top element of s1  <br>
         while s2 is NOT empty and top(s1) is greater than temp:  <br>
                Assign s1 to the value of s2  <br>
                push the value of temp in s2  <br>
        display s2   <br>


