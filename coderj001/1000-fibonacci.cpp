//   #     ###     ###     ###                                    #######                                                                                            
//  ##    #   #   #   #   #   #        #####  #  ####  # #####    #       # #####   ####  #    #   ##    ####   ####  #    #    # #    # #    # #####  ###### #####  
// # #   #     # #     # #     #       #    # # #    # #   #      #       # #    # #    # ##   #  #  #  #    # #    # #    ##   # #    # ##  ## #    # #      #    # 
//   #   #     # #     # #     # ##### #    # # #      #   #      #####   # #####  #    # # #  # #    # #      #      #    # #  # #    # # ## # #####  #####  #    # 
//   #   #     # #     # #     #       #    # # #  ### #   #      #       # #    # #    # #  # # ###### #      #      #    #  # # #    # #    # #    # #      #####  
//   #    #   #   #   #   #   #        #    # # #    # #   #      #       # #    # #    # #   ## #    # #    # #    # #    #   ## #    # #    # #    # #      #   #  
// #####   ###     ###     ###         #####  #  ####  #   #      #       # #####   ####  #    # #    #  ####   ####  #    #    #  ####  #    # #####  ###### #    # 
                                                                                                                                                                  
// The Fibonacci sequence is defined by the recurrence relation:
//
// Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
// Hence the first 12 terms will be:
//
// F1 = 1
// F2 = 1
// F3 = 2
// F4 = 3
// F5 = 5
// F6 = 8
// F7 = 13
// F8 = 21
// F9 = 34
// F10 = 55
// F11 = 89
// F12 = 144
// The 12th term, F12, is the first term to contain three digits.
//
// What is the index of the first term in the Fibonacci sequence to contain 1000 digits?


#include <bits/stdc++.h>
using namespace std;
string sum(string,string);
int main(){
    vector<string> v;
    v.push_back("1");
    v.push_back("1");
    for(int i=2;;i++){
        v.push_back(sum(v[i-2],v[i-1]));
        if(v[i].length()==10000){
            cout<<v[i]<<endl;
            printf(">>>>>>>>%d\n",i+1);
            return 0;  
        }
    }
}
string sum(string s1,string s2){
    string str="";
    reverse(s2.begin(),s2.end());
    reverse(s1.begin(),s1.end());
    int carry=0;
    for(int i=0;i<s1.length();i++){
        int sum=((s1[i]-'0')+(s2[i]-'0')+carry);
        str+=sum%10+'0';
        carry=sum/10;
    }
    for(int i=s1.length();i<s2.length();i++){
        int sum=((s2[i]-'0')+carry);
        str+=sum%10+'0';
        carry=sum/10;
    }
    if(carry)
        str+=carry+'0';
    reverse(str.begin(),str.end());
    return str;
}
