//Question Link
//https://practice.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1

int getNthFromLast(Node *head, int n)
{  
int length=0,i;

Node *temp=head;
while(temp!=NULL)
{
temp=temp->next;
length++;
}

if(length<n)
{return -1;}
temp=head;
for(i=1;i<length-n+1;i++)
{ temp=temp->next;
}
return temp->data;   
}