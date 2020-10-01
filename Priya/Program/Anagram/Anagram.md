 ## DOCUMENTATION

 ## All the algorithms are coded in Python Language
## Anagram  
<img src="https://img.shields.io/badge/-Nagarro-green" height="30">&nbsp;&nbsp;


### Problem Statement

  Two strings a and b consisting of lowercase characters are given.<br>
  Check whether two given strings are an anagram of each other or not. <br>
  **Note:**  An anagram of a string is another string that contains the same characters, only the order of characters can be different. <br>

          Sample :
        Input: a = "restful" b = " fluster " 
        Output: True 
     
  ## Solution : <br>
  ## Optimized Approach:- <br>
  (i) check the length of the both strings  <br>
  (ii) check each alphabet of the both strings <br>  
  
    
  ## Time and Space complexity  <br>
 Time Complexity :- O(n)<br>
 Space Complexity:- O(Number of distinct characters)
  ##  Pseudocode <br>
   Accept two strings (a,b) <br>
   check if the lenght (a) != (b) <br>
   then return False  <br>
   else : sort the array a and store it in a; sort array b and store it in a  <br>
       for i=0 ....len(a) <br>
           if(a[i] == b[i]) <br>
              return True  <br>
               else: return False  <br>
