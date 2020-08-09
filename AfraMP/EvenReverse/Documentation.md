# DOCUMENTATION
## Even Reverse<br>
<a><img src="https://img.shields.io/badge/-Amazon-blue" height="25">&nbsp;&nbsp;<img src= "https://img.shields.io/badge/-Interview Bit-navy" height="25">
&nbsp;&nbsp;<img src= "https://img.shields.io/badge/-CPP-red" height="25"></a><br>
**Problem Statement**<br>
Given a linked list A , reverse the order of all nodes at even positions.<br>
Return the head of the new linked list.

```
Example 1

10
1 3 5 7 9 2 4 6 8 0
```
> > 1 0 5 6 9 2 4 7 8 3
```
Example 2

4
1 2 7 6
```
> > 1 6 7 2
#### Solution<br>
```
#include <iostream>
#include <vector>

using namespace std;


struct Node{
	int data;
	Node* link;
};
int i=1;
Node *start=NULL;

// method to print 
void printList(Node* node)
{
	while(node != NULL){
		printf("%d ", node->data);
		node = node->link;
	}
	printf("\n");
}
void dfs(Node *A,int j)
{
   if(i>j||!start||!A) return;
   if(A->link) A=A->link;
   else return ;
   if(A->link) A=A->link;
   else return ;
   dfs(A,j+2);
   if(start&&i<j+2)
   {
       swap(A->data,start->data);
       i+=2;
       if(start)start=start->link;
       if(start)start=start->link;
       return ;
   }
   return ;
}

Node* evenReverse(Node* A) {
    if(A)
    start=A->link;
    else
    return A;
    i=2;
    dfs(A->link,2);
    return A;
}

// method to insert elements
void insertElement(Node** head_Pointer, int data_elem)
{
	Node* elem = (struct Node*)malloc(sizeof(struct Node));
	elem->data = data_elem;
	elem->link = *head_Pointer;
	*head_Pointer = elem;
}

int main()
{
	int n, i;
	int a[10];
	Node* head = NULL;
	printf("Enter the number of elements:\n");
	scanf("%d", &n);
	printf("Enter the elements\n");
	for(i = 0; i < n; i++){
		scanf("%d", &a[i]);
	}
	for(i = n-1; i >= 0; i--)
		insertElement(&head, a[i]);
	printf("Linked list before even reverse");
	printList(head);
	evenReverse(head);
	printf("Linked list after even reverse");
	printList(head);
	return 0;
}
	
```