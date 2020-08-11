# Documentation

## Add 1 to a number represented as Linked List
<img src="https://img.shields.io/badge/Asked in-Amazon-blue" alt="Google" />

### Problem Statement
> A number N is represented in Linked List such that each digit corresponds to a node in linked list. You need to add 1 to it.

Sample I/O
```
Input: 2999
Output: 3000
```

#### Input
> The First line contains the number of test cases, and for each test case a single line of input denotes an big number N.

#### Output
> For each test case, print the resulting number in a new line.

### Naive Approach (Iterative)
We've to add 1 to a number represented as LL and on adding 1 if the number is 9 we'll get a two digit number 1 0, 0 is our sum and 1 will be carry.
The idea is to traverse the LL from leftmost node after reversing the LL, until we reach the number where, on adding carry from previous sum there is no carry generated.
If we reach the end of LL and there is still a carry left then append it to the end of LL.
Before returning the head reverse the LL.


#### Pseudo Code
1. Reverse the given linked list
      - For example, [2]-> [9]-> [9] -> [9] is converted to [9] -> [9] -> [9] -> [2]
2. Traverse the LL from leftmost node and add 1 to it:
      - If there is a carry
          - move to the next node, Keep moving to the next node while there is a carry
3. Reverse the modified LL and return head

#### C++ Function Implementation
```cpp
Node* addOne(Node *head) 
{ 

    head = reverse(head); 
    // reverse() is a function to reverse the linked list and returns the head of modified LL
    Node* res = head; 
    Node *temp, *prev = NULL; 

    int carry = 1, sum; 

    while (head != NULL) 
    { 
        sum = carry + head->data; 

        carry = (sum >= 10)? 1 : 0; 
 
        sum = sum % 10; 

        head->data = sum; 

        temp = head; 
        head = head->next; 
    } 

    if (carry > 0) {
    	Node *ctemp = new Node(carry);
		temp->next = ctemp ;
	}
    
    head = res; 

    return reverse(head); 
} 
```
