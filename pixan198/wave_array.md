# Documentation

## Wave Array

### Problem Statement

> **Given an array of integers, sort the array into a wave like array and return it,**
> **In other words, arrange the elements into a sequence such that `a1 >= a2 <= a3 >= a4 <= a5 . . . . .`**

**Example**
```
Given [1, 2, 3, 4]

One possible answer : [2, 1, 4, 3]
2     4
 \   / \
  \ /   \
   1     3

Another possible answer : [4, 1, 3, 2]
4     3
 \   / \
  \ /   \
   1     2

```
> `NOTE`: If there are multiple answers possible, return the one thats lexicographically smallest.
> So, in example case, you will return `[2, 1, 4, 3]`

### Pseudo Code

```
This Program sorts the given array in a wave form

function wave ( Arguement givenArray ){
    Sort the givenArray using sort() function from STL
    
    swap Numbers of array in interval of two until last element is reached
    
    return sorted array
}
```
### C++ Solution

```cpp
#include <iostream>
#include <algorithm>
#include <vector>

//using namespace std;

using std::cin;
using std::cout;
using std::vector;
using std::swap;
using std::sort;

vector<int> wave(vector<int> &A) {
    sort(A.begin(),A.end());
    for(int i=0;i<A.size();i+=2)
        if(i+1<A.size())
            swap(A[i],A[i+1]);
    return A;
}

int main(){
  
  int n, temp;
  vector<int> A;
  
  cin >> n;
  
  for( int i = 0; i < n; i++ ){
    cin >> temp;
    A.push_back(temp);
  }
  
  A = wave(A);
  
  for( int i = 0; i < n; i++ ){
    cout << A[i];
  }
  
  return 0;
}
```
