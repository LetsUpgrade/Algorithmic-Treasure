//Question Link
//https://practice.geeksforgeeks.org/problems/delete-middle-of-linked-list/1

Node* deleteMid(Node* head)
{

struct Node *ptr=head;
int count=0;
while(ptr!=NULL)
{
count++;
ptr=ptr->next;
}
ptr=head;
struct Node *preptr;


for(int k=0;k!=count/2;k++)
{
preptr=ptr;
ptr=ptr->next;
}

preptr->next=ptr->next;
free(ptr);

return head;

}