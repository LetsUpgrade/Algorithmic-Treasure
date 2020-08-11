# Documentation

## Sort Binary Linked List

<a><img src= "https://img.shields.io/badge/-Amazon-orange" height="25">&nbsp;&nbsp;<img src= "https://img.shields.io/badge/-InterviewBit-violet" >
&nbsp;&nbsp;<img src= "https://img.shields.io/badge/-Python-brightgreen"></a>

#### Problem Statement

Given a Linked List A consisting of N nodes.

The Linked List is binary i.e data values in the linked list nodes consist of only 0's and 1's.

You need to sort the linked list and return the new linked list.

> > NOTE: Try to do it in constant space.

> > Problem Constraints

    1 <= N <= 105

    A.val = 0 or A.val = 1

> > Input Example

     1 -> 0 -> 0 -> 1

> > Input Example

    0 -> 0 -> 1 -> 1 -> 0

> > Output Example

    0 -> 0 -> 1 -> 1

> > Output Example

    0 -> 0 -> 0 -> 1 -> 1

> > Explanation 1:

    The sorted linked list looks like:
    0 -> 0 -> 1 -> 1

> > Explanation 2:

    The sorted linked list looks like:
    0 -> 0 -> 0 -> 1 -> 1

## Approach

Following steps can be used to sort the given linked list:

    Traverse the list and count the number of 0s, 1s. Let the counts be n1, n2 respectively.
    Traverse the list again, fill the first n1 nodes with 0, then n2 nodes with 1.

Time Complexity: O(N) where N is number of nodes in linked list.
Auxiliary Space: O(1)

The above solution does not work when these values have associated data with them.
For example, these two represent two colors and different types of objects associated with the colors and we want to sort objects (connected with a linked list) based on colors.

So, A new solution is discussed that works by changing links.

Iterate through the linked list. Maintain 2 pointers named zero and one to point to current ending nodes of linked lists containing 0 and 1 respectively.
For every traversed node, we attach it to the end of its corresponding list.
Finally we link both the lists.
To avoid many null checks, we use two dummy pointers zeroD and oneD that work as dummy headers of the two lists.

Time Complexity: O(N) where N is number of nodes in linked list.
Auxiliary Space: O(1)

#### Solution

To be added soon ... .. ...
