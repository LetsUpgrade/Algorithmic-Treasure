# Documentation

## The Celebrity Problem

<img src="https://img.shields.io/badge/Asked in-Amazon | Fab.com | Flipkart | Google | Microsoft | One97 | United Health Group | Zoho-blue" alt="Google" />

### Problem Statement

> You are in a party of N people, where only one person is known to everyone. Such a person may be present in the party, if yes, (s)he doesn’t know anyone in the party. Your task is to find the stranger (celebrity) in party.

**Expected Time Complexity:** O(N).

**Expected Auxiliary Space:** O(1).

#### Input

The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.

First Line of each test case contains a integer N denoting number of rows or columns.

Second line contains N*N space seperated values.

#### Output

ID of the person who is celebrity and -1 if there is no celebrity.

#### Sample I/O
```
Input:
2
3
0 1 0 0 0 0 0 1 0
2
0 1 1 0

Output:
1
-1
```

### Naive Approach

We will count two things about any person, first how many people (s)he knows in the party(out) and second how many people know that person(in). We will store these values for every person and according to the problem, celebrity does not know anybody at the party but everybody knows h(im/er). So, we need to find a specific pair of values in the data we stored earlier, celebrity does not know anybody means it will have `0` for how many people he/she know value and everybody knows celebrity so it will have `n-1` for how many people know that person value, everybody knows except itself so, no. of people - 1(n-1).

<img src="https://pixan198.github.io/images/celebrity_problem.svg" alt="example" />

#### Pseudo Code
```
Create two arrays in and out of size N and initialize all value with 0
// in is for how many people know that person
// out is for how many people he/she knows

Traverse the whole matrix:
    Run nested loops outer from 0 to N and inner from 0 to N
    //inner loop for "in" and outer loop for "out" array
    For every value in matrix add the value to both array with respect to its iterator
Traverse both array at same time and check for the pair in[x] = (N-1) && out[x] = 0
    If found:
      return x
    If not found:
      return -1
```

#### C++ Function Implementation
```cpp
int getId(int M[MAX][MAX], int n)
{
    int in[n]={0},out[n]={0}; 
      
    for(int i=0; i<n; i++) 
    { 
        for(int j=0; j<n; j++) 
        { 
            int x = M[i][j]; 
              
            out[i]+=x; 
            in[j]+=x; 
        } 
    } 
      
    for(int i=0; i<n; i++) {
    	if(in[i] == n-1 && out[i] == 0) { 
        	return i;
    	}
    }
      
    return -1;
}
```
