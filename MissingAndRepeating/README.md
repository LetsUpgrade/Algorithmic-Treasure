# DOCUMENTATION
## Find Missing And Repeating<br>
![Github Logo](https://camo.githubusercontent.com/8cf04a6dcc08ed39b13778a727819581acc566e5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d416d617a6f6e2d626c7565)
![Github Logo](https://camo.githubusercontent.com/e579fafbb1bdb9e720e3f9c7eee3874223ef71e5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d507974686f6e2d627269676874677265656e)
![Github Logo](https://camo.githubusercontent.com/d4fa9897ff15062a43ea2ef2957d088d3a5d9035/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d4c656574636f64652d76696f6c6574)<br>
 **Problem Statement**<br>
 Given an unsorted array of size N of positive integers. One number 'A' from set {1, 2, …N} is missing and one number 'B' occurs twice in array. Find these two numbers.
 <br>Also, expected solution is O(n) time and constant extra space.
```
Example 1

2
2
2 2
3
1 3 3
```
> > 2 1<br>
> > 3 2
```
Example 2

3
2
1 1
3
2 2 1
```
> > 1 2<br>
> > 2 3
#### Solution<br>
In the above program we are supposed to find the duplicate number and the number missing the the range of N with a time complexity not exceeding O(n). The pseudocode for the above program is as follows:
#### Psuedocode<br>
PROGRAM missing_and_repeat<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Read T, N, Arr<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; SET B = 0<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; SET A = 0<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; FOR each element in Arr<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; IF T[element] >= 0 THEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; T[element] = -1<br></br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ELSE<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; B = element<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; END IF<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;END FOR<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; FOR i from 1 to N + 1 // i += 1<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; IF T[i] = 0<br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  A = i<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; BREAK<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; END IF<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; END FOR<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; PRINT B, A<br>
END<br>
