# Documentation

## **Max Sum Contiguous Subarray**

Asked in:  <a><img src= "https://img.shields.io/badge/-Goldman Sachs-orange" height="25">&nbsp;&nbsp;
<img src= "https://img.shields.io/badge/-Facebook-blue" height="25">&nbsp;&nbsp;
<img src= "https://img.shields.io/badge/-PayTm-skyblue" height="25">&nbsp;&nbsp;
<img src= "https://img.shields.io/badge/-Paypal-navy" height="25">&nbsp;&nbsp;
<img src= "https://img.shields.io/badge/-Yahoo-purple" height="25">&nbsp;&nbsp;
<img src= "https://img.shields.io/badge/-Microsoft-yellow" height="25">&nbsp;&nbsp;
<img src= "https://img.shields.io/badge/-LinkedIn-red" height="25">&nbsp;&nbsp;
<img src= "https://img.shields.io/badge/-Amazon-black" height="25">&nbsp;&nbsp;
<img src= "https://img.shields.io/badge/-InterviewBit-skyblue" >&nbsp;&nbsp;
<img src= "https://img.shields.io/badge/-CPP-red">&nbsp;&nbsp;


### Problem Statement 
Find the contiguous subarray within an array, A of length N which has the largest sum.


 **Input Format:**
   
     The first and the only argument contains an integer array,A.
 
 **Output Format:**
   
     Return an integer representing the maximum possible sum of the contiguous subarray.

**Constraints:**

     1 <= N <= 1e6

    -1000 <= A[i] <= 1000

**For example:**

    Input 1:
        A = [1, 2, 3, 4, -10]

    Output 1:
         10

>> ***Explanation 1:***
The subarray [1, 2, 3, 4] has the **maximum possible sum of 10**.

    Input 2:
        A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    Output 2:
         6

>>***Explanation 2:***
 The subarray [4,-1,2,1] has the **maximum possible sum of 6**.
 
 
 
 ## Solution:-
 
**Bruteforce Approach :** 

      1) Use two loops. 
      2) The outer loop picks the beginning element,
         the inner loop finds the maximum possible sum with first element picked by outer loop 
         and compares this maximum with the overall maximum.
      3) At last, return the overall maximum.
       
>>**Time complexity :** *O(n^2)*

**Kadane’s Algorithm :**
 
       MaxSum(a[],size)
         1) Initialize:
               max = 0
               sum = 0
         2) Loop for each element of the array
              (a) sum = sum + a[i]
              (b) if(sum<0) then 
                   initialize sum=0
              (c) else if(max<sum)
                    then max=sum
         3) return max
         
>>**Time Complexity:** *O(n)* 


>>**Algorithmic Paradigm:** *Dynamic Programming*

***[Reference](https://www.interviewbit.com/problems/max-sum-contiguous-subarray/)***
