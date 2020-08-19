# Documentation

## **Stairs**

Asked in: 
<img src= "https://img.shields.io/badge/-Amazon-orange" height="25">&nbsp;&nbsp;
<img src= "https://img.shields.io/badge/-Intel-blue" height="25">&nbsp;&nbsp;
<img src= "https://img.shields.io/badge/-Morgan Stanley-gray" height="25">&nbsp;&nbsp;
<img src= "https://img.shields.io/badge/-Interviewbit-skyblue">&nbsp;&nbsp;
<img src= "https://img.shields.io/badge/-Python-brown">&nbsp;&nbsp;


### Problem Statement 
You are climbing a stair case and it takes A steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**Input Format :** 
          The first and the only argument contains an integer A, the number of steps.

**Output Format :**
          Return an integer, representing the number of ways to reach the top.

**Constrains :** 
         ```1 <= A <= 36```

**Example 1 :**

      Input  :  A = 2 
      
      Output :  2
      
      Explanation : [1, 1], [2] 

**Example 2 :**
      
      Input : A = 3 
      
      Output :3
      
      Explanation : [1 1 1], [1 2], [2 1]



        
 ### Solution:

**DP Fibonacci**
   
   
   To each a specific stair **x**, we can either climb **1** stair from `x-1`, or **2** stairs from `x-2`. 
          Therefore, suppose `dp[i]` records the number of ways to reach stair **i**, it's a *Fibonacci Array*.
                    
                    dp[i] = dp[i-1]+dp[i-2] 
          
   The base case is to reach the first stair, we only have one way to do it so ``dp[1] = 1.``
   Besides, since only dp elements we used is most recent two elements, we can use two pointer to save using of dp array. 

****
 
           
 >>Time complexity : **O(n)**

***[For Reference](https://www.interviewbit.com/problems/stairs/)***
