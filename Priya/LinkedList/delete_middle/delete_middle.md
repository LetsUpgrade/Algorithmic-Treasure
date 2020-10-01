
 ## DOCUMENTATION

 ## All the algorithms are coded in Python Language
## Delete Middle Of Linked List 
<img src="https://img.shields.io/badge/-Amazon-blue" height="30">&nbsp;&nbsp;
<img src= "https://img.shields.io/badge/-Flipcart-yellow" height="30">&nbsp;&nbsp;
<img src= "https://img.shields.io/badge/-Microsoft-Brown" height="30">&nbsp;&nbsp;<br>

### Problem Statement

A singly linked list is given.The task is to delete middle of the linked list according to the given two conditions :<br>
If there are odd number of nodes given : linked list is **1->2->3->4->5** then linked list should be modified to **1->2->4->5**.<br>
and If there are even nodes, then there would be two middle nodes, we need to delete the second middle element.<br>
Given linked list is **1->2->3->4->5->6** then it should be modified to **1->2->3->5->6**.<br>
If the input linked list is NULL or has 1 node, then it should return NULL <br>
           
           Sample :
          Input: [1 -> 2 -> 3-> 4-> 5]  Input: [1 -> 2 -> 3-> 4-> 5 -> 6]    
          Output: [1 ->2 ->4 -> 5 ]     Output : [1 -> 2 -> 3-> 5 -> 6] 
     
  ## Solution : <br>
  ## Optimized Approach:- <br>
   There are three pointers **(prev , i , j)** which are initially initilized to **None , head , head** respectively.<br>
    At the beginning the **i** and **j** pointer will point the very first node <br>
    check if **j** pointer and **j.next** pointer is valid  <br>
    then increase the **j** pointer to **2 steps** ahead  <br>
    store the adress of **i** in **prev** pointer and  increase **i** pointer to **1 step** ahead. <br>
    connect the address of **prev pointer** to the **next address** after i pointer.
    
  ## Time and Space complexity  <br>
   Time Complexity :- O(n)<br>
   Space Complexity:- O(1)
  ##  Pseudocode <br>
  prev,i,j= none, head ,head  <br>
  while(j and j.next): <br>
  j =j.next.next <br>
  prev = i <br>
  i  =i.next   <br>
  prev.next = i.next <br>
  return head 
