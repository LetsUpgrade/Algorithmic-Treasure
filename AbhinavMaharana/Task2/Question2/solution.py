#--------------------------------------------------------------------------------------------------------------------------------#
#A linked list is a linear data structure where each element is a separate object.                                               #
#Linked list elements are not stored at contiguous location; the elements are linked using pointers.                             #
#Each node of a list is made up of two items - the data and a reference to the next node. The last node has a reference to null. #
# The entry point into a linked list is called the head of the list. It should be noted that head is not a separate node,        #
# but the reference to the first node. If the list is empty then the head is a null reference.                                   #
#Linked List Representation                                                                                                      # 
#--------------------------------------------------------------------------------------------------------------------------------#
# This is the final and full code and the explanation is in the documentation. Nothing more can be add in this code. I have compiled it and it is the full code and it runned there.#
class Solution:
    #-----------------------------------#
    # A : head node of linked list      #
    #-----------------------------------#
    def solve(self, A):
        #---------------------------#
        # head node A is equal to H #
        #---------------------------#
        h=A
        
        #---------------------------#
        #    Getting variable       #
        #---------------------------#
        a=0
        b=0
        c=0

        #-------------------------------#
        #    Creating a while loop      #
        #-------------------------------#
        
        while h:
            if h.val==0:
                a+=1
            else:
                b+=1
            h=h.next    
            
        h=A
        while h:
            if c<a:
                c+=1
                h.val=0
            else:
                h.val=1
            h=h.next
        
        #-------------------------------#
        #    Returning the head node    #
        #-------------------------------#
            
        return A

