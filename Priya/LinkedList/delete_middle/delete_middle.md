 ##  DOCUMENTATION



<p> <b> All the algorithms are coded in Python Language</b></p>
<p><b> Solution:Question 1 </b> </p>
 <p> <b> 1.  Optimized Approach:- </b> <br>
    There are three pointers (prev , i , j) which are initially initilized to None , head , head respectively.<br>
    At the beginning the i and j pointer will point the very first node <br>
    check if j pointer and j.next pointer is valid  <br>
    then increase the j pointer to 2 steps ahead  <br>
    store the adress of i in prev pointer and  increase i pointer to 1 step ahead. <br>
    connect the address of prev pointer to the next address after i pointer.
  </p>
 <p><b>  2. Time and Space complexity :- </b><br>
         Time Complexity :- O(n)<br>
         Space Complexity:- O(1)
 </p>
 <p> <b> 3. Pseudocode </b><br>
         prev,i,j= none, head ,head         <br>
         while(j and j.next): <br>
         j =j.next.next <br>
         prev = i <br>
         i  =i.next   <br>
         prev.next = i.next <br>
         return head 
         
          >>  OUTPUT
          Input: [1 -> 2 -> 3-> 4-> 5]  Input: [1 -> 2 -> 3-> 4-> 5 -> 6]    
          Output: [1 ->2 ->4 -> 5 ]        Output : [1 -> 2 -> 3-> 5 -> 6] 
          
  </p>
