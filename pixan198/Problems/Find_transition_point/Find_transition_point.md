# Documentation

## Find Transition Point

<img src="https://img.shields.io/badge/Asked in-Amazon-blue" alt="Amazon" />

### Problem Statement
> You are given a sorted array containing only numbers 0 and 1. Find the transition point efficiently. The transition point is a point where "0" ends and "1" begins (0 based indexing).
> 
> Note that, if there is no "1" exists, print -1.
> 
> Note that, in case of all 1s print 0.

**Expected Time Complexity:** O(LogN).

**Expected Auxiliary Space:** O(1).

#### Input

The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
First Line of each test case contains N (number of elements in array).
Second line contains N space seperated integers.

#### Output

Print Transition point or -1 for all 0s and 0 for all 1s.

#### Sample I/O
```
Input:
1
5
0 0 0 1 1

Output:
3
------------------------------

Input:
1
4
0 0 0 0

Output:
-1
```

### Naive Approach

We can traverse the array and return the index of first 1 we find.

Time Complexity: O(N)

Space Complexity: O(1)

#### Pseudo Code
```
traverse the array from start to end:
    Check if the current element is '1'
        IF Yes:
          Return index
          Break loop
        IF No:
          Keep Traversing
Print Index of First 1
```

#### C++ Function Implementation

```cpp
int transitionPoint(int arr[], int n) {
    for(int i=0; i<n ;i++){
		if(arr[i]==1){
	  		return i;
		}
	}
	
    return -1; 
}
```
