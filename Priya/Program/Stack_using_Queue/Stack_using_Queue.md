 ## DOCUMENTATION
 
 ## All the algorithms are coded in Python Language
## Stack using two Queues
<img src="https://img.shields.io/badge/-Accolite-red" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-Adobe-yellow" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-Amazon-orange" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-Cisco-blue" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-CouponDunia-purple" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/- D E Shaw -brown" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-Grofers-red" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-Kritikal Solution-blue" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-Oracle-orange" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-OYO Rooms-yellow" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-Snapdeal-red" height="30">&nbsp;&nbsp;



### Problem Statement
   Implement a Stack using two queues q1 and q2.
          
        Sample :
        Input: 
                 push(20)
                 push(4)
                 pop()
                 push(7)
                 pop()
         
         Output: 4 7
       
      Explanation:
     push(20) : the stack will be {20}
     push(4)  : the stack will be {20 4}
     pop()    : poped element will be 4 the 
                stack will be {20}
     push(7)  : the stack will be {20 7}
     pop()    : poped element will be 7
 
 ## Solution : <br>
  ## Optimized Approach:- <br>
 (i) create two queue **(q1 , q2)** <br>
         (ii) enqueue the elements to the front of **q1**.<br>
         (iii) **pop** operation to dequeue from **q1**  <br>
         (iv) **q2** is used to enqueue at the front of **q1**. <br>
          (v) return the popped element  <br>
    
  ## Time and Space complexity  <br>
 Time Complexity :- Push() - O(1) ; POP() -  O(N) <br>
 Space Complexity:- PUSH() -O(1) ; POP() - O(1)
  
  ##  Pseudocode <br>
   Create two queue (q1, q2) <br>
   push(x): [x is the element to be pushed in the stack] <br>
   Enqueue x to q2 <br>
         One by one dequeue everything from q1 and enqueue to q2. <br>
         Swap the names of q1 and q2 <br>
         pop(s): <br>
        Dequeue an item from q1 and  <br>
         return the popped element <br>
