# Documentation

<a><img src="https://img.shields.io/badge/-Google-orange" height="25px">&nbsp;&nbsp;<img src="https://img.shields.io/badge/-Microsoft-blue" height="25">&nbsp;&nbsp;<img src="https://img.shields.io/badge/-Cpp-red"></a> 

### problem statement 1
## max_min_sum

Given an array A of size N . You need to find sum of maximum and minimum element in the given array.
Note: you should make minimum number of comparisons.

Problem Constraitns
1 <= N <= 105
-109 <= A[i] <= 109

Input Format
First and only argument is an integer array A of size N.

Output Format
Return an integer denoting the sum of maximum and minimum element in the given array.

Example Input
Input 1:
A = [-2,1,-4,5,3]

Input 2:
A=[1,3,4,1]

Example Output 
Output 1:
1

Output 2:
5

Example Explanation
Explanation 1:
maximum element is 5 and minimum element is -4. ((5+(-4))=1).

Explanation 2:
maximum element is 4 and mimimum element is 1. ((4+1)=5).


### Solution

---Cpp
#include<iostream>
#include<vector>
#include<algorithm>
  
using namespace std;

class solution
{
public:
     int find_sum(vector <int>& arr)
       {sort(arr.begin(), arr.end())
        return arr[0]+arr[arr.size()-1]
       }
 };
 
 int main()
{
    vector<int>arr
    int key,size;
    cin>>size;
    while(size--)
    { cin>>key;
      arr.push_back(key);
    }
    solution sol;
    cout << sol.find_sum(arr) << endl;
    return 0;
}  
  
  
  
### problem statement 2)
## OnePlus

Given a non-negative number represented as an array of digits, 
add 1 to the number (increment the number represented by the digits).
The digits are stored such that the most significant digit is at the head of the list.

Example:
If the vector has [1,2,3]
the returned vector should be [1,2,4]
as 123+1=124

Note: Certain things are intentionally left unclear in this question which you should practice asking the interviewer.
For example, for this problem , following are some good questions to ask:
Q : Can the input have 0's before the most significant digit ? Or in other words, 0 1 2 3 is valid input ?
A : For the purpose of this question , Yes
Q : Can the output have 0's before the most significant digit ? Or in the other words, 0 1 2 4 is valid output ?
A : For the purpose of this question , No. Even if the input has zeroes before the most significant digit 

      
 ### solution 
 
 ---Cpp
 #include<iostream>
 #include<vector>
 #include<algorithm>
  
 using namespace std;
 
 class solution
 {public:
        vector <int> plusOne(vector <int>& arr)
       {
          int n= arr.size();
          arr [n-1] += 1;
          int hand= arr[n-1]/10;
          arr[n-1]=arr[n-1]%10;
          
          for(int i=n-2; i>0; i--)
          { 
            if(hand==1)
            {
               arr[i] += 1;
               hand= arr[i]/10;
               arr[i]=arr[i]%10;
            }  
           }
           
           if(hand==1)
            arr.insert(arr.begin(),1);
            return arr;
        }
  };
  
  int main()
  {  vector <int> arr;
     int key,size;
     cin >> aize;
     while(size--)
     {  cin>>key;
        arr.push_back(key);
     }
     solution sol;
     vector <int> arr2;
     arr2= sol.plusOne(arr);
     for(int i=0; i<arr2.size(); i++)
     {  
           cout << arr2[i]  << " ";                   
     }
     return 0;                          
  }  

