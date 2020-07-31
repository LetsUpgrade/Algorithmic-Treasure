#include <iostream>
using namespace std;

int Max_sum(int a[],int size){
  int sum=0;
  int max=0;
  for(int j=0;j<size;j++)
  { sum+=a[j];
    if(sum<0)
    sum=0;
    else if(max<sum)
    max=sum;
  }
  return max;
}

int main() {
  int n;
  cin>>n;
  int arr[n];
  // Input of Array
  for(int i=0;i<n;i++)
  cin>>arr[i];

  cout<<Max_sum(arr,n);
  return 0;
}