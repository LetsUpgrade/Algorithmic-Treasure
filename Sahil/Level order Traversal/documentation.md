# Documentation

## **Level Order**

Asked in: 
<img src= "https://img.shields.io/badge/-Goldman Sachs-orange" height="25">&nbsp;&nbsp;
<img src= "https://img.shields.io/badge/-Facebook-blue" height="25">&nbsp;&nbsp;
<img src= "https://img.shields.io/badge/-Groupon-green" height="25">&nbsp;&nbsp;
<img src= "https://img.shields.io/badge/-Interviewbit-skyblue">&nbsp;&nbsp;
<img src= "https://img.shields.io/badge/-Python-brown">&nbsp;&nbsp;


### Problem Statement 
Given a binary tree, return the level order traversal of its nodes’ values. (ie, from left to right, level by level).


**Example :**

     Input: Given binary tree

              3
             / \
            9  20
              /  \
             15   7
          

     Output:
             [
                  [3],
                  [9,20],
                  [15,7]
                ]

       
 ### Solution:

**Using Queue**

        printLevelorder(tree)
        1. create an empty queue q and append root to queue
        2. while there are nodes in the queue, 
            pop queue(0), add queue(0).val to current ans list 
            and append queue(0)'s children to queue
            append ans to final_list and reset ans = []
          end of loop
         3.return final_list
         
        


****
 
           
 >>Time complexity : **O(n)**

***[For Reference](https://www.interviewbit.com/problems/level-order/)***
