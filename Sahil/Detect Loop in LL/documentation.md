# Documentation

## **Detect Loop in linked list**

Asked in:  <a><img src= "https://img.shields.io/badge/-DEShaw-red" height="25">&nbsp;&nbsp;
<img src= "https://img.shields.io/badge/-Amazon-yellow" height="25">&nbsp;&nbsp;
<img src= "https://img.shields.io/badge/-Paytm-blue" height="25">&nbsp;&nbsp;
<img src= "https://img.shields.io/badge/-GeekforGeeks-darkgreen">&nbsp;&nbsp;
<img src= "https://img.shields.io/badge/-CPP-brown">&nbsp;&nbsp;


### Problem Statement 
Given a linked list of N nodes. The task is to check if the the linked list has a loop. Linked list can contain self loop.

**Constraints:**

              1 <= N <= 104
              1 <= Data on Node <= 103


**Example 1 :**

        Input:
                N = 3
                value[] = {1,3,4}
                x = 2
        
        Output: True
        
        
        Explanation: 
                      In above test case N = 3.
                      The linked list with nodes N = 3 is given.
                      Then value of x=2 is given which means last node is connected with xth node of linked list.
                      Therefore, there exists a loop.

**Example 2 :**

        Input:
                N = 4
                value[] = {1,8,3,4}
                x = 0
                
        Output: False
        
        Explanation: 
                    For N = 4 ,x = 0 means then lastNode->next = NULL, 
                    then the Linked list does not contains any loop.
        
        
 ### Solution:


**Floyd’s Cycle-Finding Algorithm :**
  
          Traverse linked list using two pointers.
          Move one pointer(slow_p) by one and another pointer(fast_p) by two. 
          If these pointers meet at the same node then there is a loop. If pointers do not meet then linked list doesn’t have a loop.


          
           
 >>Time complexity : **O(n)**  & Auxiliary Space : **O(1)**.

***[For Reference](https://practice.geeksforgeeks.org/problems/detect-loop-in-linked-list/1)***
