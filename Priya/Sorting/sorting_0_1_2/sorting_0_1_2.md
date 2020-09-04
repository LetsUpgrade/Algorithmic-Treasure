
 ## DOCUMENTATION
 
## All the algorithms are coded in Python Language
## Sort an array of 0s, 1s and 2s
<img src="https://img.shields.io/badge/-Adobe-red" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-Amazon-yellow" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-Hike-orange" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-MakeMyTRip-blue" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-MAQ Software -purple" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/- Microsoft -brown" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-Morgan Stanley-green" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-Ola Cabs-blue" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-OYO Rooms-orange" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-Paytm-yellow" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-Qualcomm-red" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-Samsung-green" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-SAP Labs-yellow" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-Snapdeal-orange" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-Walmart-blue" height="30">&nbsp;&nbsp;
<img src="https://img.shields.io/badge/-Yatra.com-purple" height="30">&nbsp;&nbsp;



### Problem Statement
   An array of size N containing 0s, 1s, and 2s is given. Sort the array in ascending order.


          
       Sample :
       Input: n=9 arr1 = [2,1,1,0,0,2,1,0,2] 
       Output:           [0,0,0,1,1,1,2,2,2]
 
 ## Solution : <br>
  ## Optimized Approach:- <br>
 (i) Count the number of 0s , 1s , 2s in the array .<br>
 (ii) Store all the 0s from the beginning , next store all 1s and then store all the 2s at the end.<br>
    
  ## Time and Space complexity  <br>
  Time Complexity :- O(n)<br>
  Space Complexity:- O(1) <br>
  
  ##  Pseudocode <br>
  def sort (arr , n ): <br>
             c0,c1,c2 =0,0,0 <br>
             for i 0 .... n: <br>
                 count the number of 0 ;c0<br>
                  count the number of 1 ;c1<br>
                  count the number of 2 ;c2 <br>
              update the value of i ; i=0  <br>
                  store  all the  0s at the beginning <br>
                  then store all the 1s <br>
                  finally store all the 2s <br>
               display the sorted array
