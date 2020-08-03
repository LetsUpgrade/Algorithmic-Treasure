# Documentation

## Find Duplicate in Array

<img src="https://img.shields.io/badge/Asked in-Amazon, VMWare, Riverbed-blue" alt="Google" />

### Problem Statement

> **Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less than O(n) space and traversing the stream sequentially O(1) times**

**Sample I/O**
```
Input: [3, 4, 1, 4, 1]

Output: 1
```

> `NOTE`: If there are multiple possible answers ( like in the sample case above ), output any one.

> If there is no duplicate, output `-1`

### Naive Approach

A naive approach could be to count all elements and store them in an array, and when we encounter any element which is occurring more than one then we return it.
This solution takes O(n) time and O(n) auxiliary space.

#### Pseudo Code

```
This Program returns duplicate element in an array

function repeatedNumber ( Arguement givenArray ){
    
    Define an array "count" of size (givenArray - 1)
    Initialize all elements of count with 0
    
    traverse the givenArray and increase the count of elements of givenArray corresponding to that index number in count array
    
    If(count[iterator] > 1){
        return count[iterator]
    }
    
    return -1
}
```

> #### C++ Function Implementation

```cpp
int repeatedNumber(const vector<int> &A) {
    vector<int> count(A.size()-1, 0);
    
    for(int i=0; i<A.size(); i++)
    {
        count[A[i]-1]++;
        if(ret[A[i]-1]>1) return A[i];
    }
    
    return -1;
}
```

### Optimized Approach (Space Optimization)



