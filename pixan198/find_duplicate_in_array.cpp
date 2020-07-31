#include <iostream>
#include <algorithm>
#include <vector>

//using namespace std;

using std::cin;
using std::cout;
using std::vector;
using std::swap;
using std::sort;

int repeatedNumber(const vector<int> &A) {
    
    vector<int> ret(A.size()-1, 0);
    
    for(int i=0; i<A.size(); i++){
        ret[A[i]-1]++;
        if(ret[A[i]-1]>1) return A[i];
    }
    return -1;
}

int main(){
  
  int n, temp;
  vector<int> A;
  
  cin >> n;
  
  for( int i = 0; i < n; i++ ){
    cin >> temp;
    A.push_back(temp);
  }
  
  cout << repeatedNumber(A);
  
  return 0;
}
