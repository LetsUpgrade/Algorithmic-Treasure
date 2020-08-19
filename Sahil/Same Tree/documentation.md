# Documentation

## **Identical Binary Trees**

Asked in: 
<img src= "https://img.shields.io/badge/-Amazon-orange" height="25">&nbsp;&nbsp;
<img src= "https://img.shields.io/badge/-Interviewbit-skyblue">&nbsp;&nbsp;
<img src= "https://img.shields.io/badge/-Python-brown">&nbsp;&nbsp;


### Problem Statement 
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

Return ```0 / 1``` ( 0 for false, 1 for true ) for this problem


**Example 1 :**

        Input : 
                 1       1
                / \     / \
               2   3   2   3

        Output : 
                1 or True



        
 ### Solution:

**Recursion Approach**

  Check if p and q nodes are not None, and their values are equal. If all checks are OK, do the same for the child nodes recursively.
      
        1. If both trees are empty then return 1.
        2. Else If both trees are non -empty
                Check data of the root nodes (tree1->data == tree2->data)
                Check left subtrees recursively i.e., call sameTree(tree1->left_subtree, tree2->left_subtree)
                Check right subtrees recursively i.e., call sameTree(tree1->right_subtree, tree2->right_subtree)
                If the values returned in the above three steps are true then return 1.
        3. Else return 0 (one is empty and other is not).
        
  
  
**Iteration Approaach**

Start from the root and then at each iteration pop the current node out of the deque. Then do the same checks as in the recursive approach:

        if p and q are not None,

        p.val == q.val,

        and if checks are OK, push the child nodes.



****
 
           
 >>Time complexity : **O(n)**

***[For Reference](https://www.interviewbit.com/problems/identical-binary-trees/)***
