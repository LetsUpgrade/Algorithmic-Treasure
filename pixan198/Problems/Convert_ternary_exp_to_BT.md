# Documentation

## Convert Ternary Expression to Binary Tree

> Given a string that contains ternary expressions. The expressions may be nested. You need to convert the given ternary expression to a binary Tree and return the root.

### Input

First line of input contains of test case T. The only line of test case consists of String s.

### Output

Preorder traversal of Tree formed.

### Constraints
```
1 <= T <= 100
1 <= |String| <= 100
```

### Sample I/O
```
Input:
2
a?b:c
a?b?c:d:e

Output:
a b c
a b c d e
```
<div>
<img style="display:inline-block;" src="https://pixan198.github.io/images/treeabc.svg" alt="a,b,c tree image"/>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
<img style="display:inline-block;" src="https://pixan198.github.io/images/treeabcde.svg" alt="a,b,c tree image"/>
</div>
