<html>
  <head>## Documentation ## </head>
  <body>
  <div>
        <p> <b>**Algorithmic Treasure ** </b></p>
        <p><b>**Project ID: 19**</b></p>
   </div>
    <div>

<p> <b> All the algorithms are coded in Python Language</b></p>
<p><b> Solution: <i>Question 1 </i> :Union of two arrays </b> </p>
 <p> <b>1.  Optimized Approach:-</b> <br>
         (i) Accept elements in  both the array(s) and store their lenght in two separate variable.<br>
         (ii) Merge the two array using "+" operator and store it in a variable .<br>
         (iii) sort the merged array using "sorted() " function  <br>
         (iv) store the sorted merged array in set [Since set does not contain duplicate elements ]  <br>
         (v)  return the final array.
  </p>
 <p> <b>  2. Time and Space complexity :-</b><br>
         Time Complexity :- O(m+n)<br>
         Space Complexity:- O(m+n)
 </p>
 <p> <b>3. Pseudocode </b> <br>
         def function(arr1, arr2 , M ,N):<br>
            result = arr1 + arr2 <br>
           return sorted(set(result))  <br>     
         
         
          >>  OUTPUT
          Input: M=7 arr1 = [1,2,2,4,5,5,6] 
          Input: N=7 arr2 = [6,6,7,7,8,9,9]
          Output: {1,2,4,5,6,7,8,9}
  </p>
<p><b> Solution: <i>Question 2 </i> : Sort an array of 0s, 1s and 2s  </b> </p>
 <p> <b>1.  Optimized Approach:-</b> <br>
         (i)Count the number of 0s , 1s , 2s in the array .<br>
         (ii) Store all the 0s from the beginning , next store all 1s and then store all the 2s at the end.<br>
  </p>
 <p> <b> 2. Time and Space complexity :- </b><br>
         Time Complexity :- O(n)<br>
         Space Complexity:- O(1)
 </p>
 <p> <b>3. Pseudocode </b><br>
         def sort (arr , n ): <br>
             c0,c1,c2 =0,0,0 <br>
             for i 0 .... n: <br>
                 count the number of 0 ;c0<br>
                  count the number of 1 ;c1<br>
                  count the number of 2 ;c2 <br>
              update the value of i ; i=0  <br>
                  store  all the  0s at the beginning <br>
                  then store all the 1s <br>
                  finally store all the 2s <br>
               display the sorted array
              
     
          >>  OUTPUT
          Input: n=9 arr1 = [2,1,1,0,0,2,1,0,2] 
          Output: [0,0,0,1,1,1,2,2,2]
  </p>
  
<p><b> Solution: <i>Question 3 </i> : Sort a Stack   </b> </p>
 <p> <b>1.  Optimized Approach:-</b> <br>
         (i) create two stack ( s1 , s2 ) and a temporary variable (temp)<br>
         (ii) the original stack (s1) should be greater than 0 <br>
         (iii) assign temp to  the top element of the original stack ., then push  temp value  into the another stack s2.
         (iv) Now, again assign temp to the next top element of the original stack 
         (v) check if the temp value if greater than the s2 
              &npbs then  push the temp value to original stack s1
              else push the temp value to s2
         (vi) return s2
  
  </p>
 <p> <b>  2. Time and Space complexity :-</b> <br>
         Time Complexity :- O(n)<br>
         Space Complexity:- O(1)
 </p>
 <p> <b>3. Pseudocode </b> <br>
         def sort (arr , n ): <br>
             c0,c1,c2 =0,0,0 <br>
             for i 0 .... n: <br>
                 count the number of 0 ;c0<br>
                  count the number of 1 ;c1<br>
                  count the number of 2 ;c2 <br>
              update the value of i ; i=0  <br>
                  store  all the  0s at the beginning <br>
                  then store all the 1s <br>
                  finally store all the 2s <br>
               display the sorted array
              
     
          >>  OUTPUT
          Input: n=9 arr1 = [2,1,1,0,0,2,1,0,2] 
          Output: [0,0,0,1,1,1,2,2,2]
  </p>
  <p><b> Solution: <i>Question 4 </i> : Stack using 2 queue   </b> </p>
 <p> <b>1.  Optimized Approach:-</b> <br>
         (i)Count the number of 0s , 1s , 2s in the array .<br>
         (ii) Store all the 0s from the beginning , next store all 1s and then store all the 2s at the end.<br>
  </p>
 <p> 2. Time and Space complexity :-<br>
         Time Complexity :- O(n)<br>
         Space Complexity:- O(1)
 </p>
 <p> 3. Pseudocode <br>
         def sort (arr , n ): <br>
             c0,c1,c2 =0,0,0 <br>
             for i 0 .... n: <br>
                 count the number of 0 ;c0<br>
                  count the number of 1 ;c1<br>
                  count the number of 2 ;c2 <br>
              update the value of i ; i=0  <br>
                  store  all the  0s at the beginning <br>
                  then store all the 1s <br>
                  finally store all the 2s <br>
               display the sorted array
              
     
          >>  OUTPUT
          Input: n=9 arr1 = [2,1,1,0,0,2,1,0,2] 
          Output: [0,0,0,1,1,1,2,2,2]
          </p>
          
           <p><b> Solution: <i>Question 5 </i> : Anagram    </b> </p>
 <p> <b>1.  Optimized Approach:-</b> <br>
         (i)Count the number of 0s , 1s , 2s in the array .<br>
         (ii) Store all the 0s from the beginning , next store all 1s and then store all the 2s at the end.<br>
  </p>
 <p> 2. Time and Space complexity :-<br>
         Time Complexity :- O(n)<br>
         Space Complexity:- O(1)
 </p>
 <p> 3. Pseudocode <br>
         def sort (arr , n ): <br>
             c0,c1,c2 =0,0,0 <br>
             for i 0 .... n: <br>
                 count the number of 0 ;c0<br>
                  count the number of 1 ;c1<br>
                  count the number of 2 ;c2 <br>
              update the value of i ; i=0  <br>
                  store  all the  0s at the beginning <br>
                  then store all the 1s <br>
                  finally store all the 2s <br>
               display the sorted array
              
     
          >>  OUTPUT
          Input: n=9 arr1 = [2,1,1,0,0,2,1,0,2] 
          Output: [0,0,0,1,1,1,2,2,2]
          </p>
          
  
  </body>

