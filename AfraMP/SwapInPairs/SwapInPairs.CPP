#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

struct Node{
	int data;
	Node* link;
};

// method to Swap the elements in pairs
void Swap(Node* head)
{
	Node* temp = head;
	int *a, temp1;
	int *b;
	while(temp != NULL && temp->link != NULL){
	    a = &temp->data;
	    b = &temp->link->data;
		temp1 = *a;
		*a = *b;
		*b = temp1;
		temp = temp->link->link;
	}
}

// Insert the elements 
void insertElement(Node** head_Pointer, int data_elem)
{
	Node* elem = (struct Node*)malloc(sizeof(struct Node));
	elem->data = data_elem;
	elem->link = (*head_Pointer);
	*head_Pointer = elem;
}

// method to print the elements
void printList(Node* node)
{
	while(node != NULL){
		printf("%d ", node->data);
		node = node->link;
	}
	printf("\n");
}

int main()
{
	int n, i;
	int a[10];
	Node* start = NULL;
	printf("Enter the number of elements:\n");
	scanf("%d", &n);
	printf("Enter the elements\n");
	for(i = 0; i < n; i++){
		scanf("%d", &a[i]);
	}
	for(i = n-1; i >= 0; i--)
		insertElement(&start, a[i]);
	printf("Linked list before swapping\n");
	printList(start);
	printf("Linked list after swapping\n");
	Swap(start);
	printList(start);
	getch();
	return 0;
}