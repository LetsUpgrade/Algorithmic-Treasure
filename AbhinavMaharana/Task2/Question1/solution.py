#--------------------------------------------------------------------------------------------------------------------------------#
#A linked list is a linear data structure where each element is a separate object.                                               #
#Linked list elements are not stored at contiguous location; the elements are linked using pointers.                             #
#Each node of a list is made up of two items - the data and a reference to the next node. The last node has a reference to null. #
# The entry point into a linked list is called the head of the list. It should be noted that head is not a separate node,        #
# but the reference to the first node. If the list is empty then the head is a null reference.                                   #
#Linked List Representation                                                                                                      # 
#--------------------------------------------------------------------------------------------------------------------------------#
class Solution:
    def reverseList(self, A, B):
        #-------------------------------------#
        #  Assigning current pointer to start #
        #-------------------------------------#
        current = A
        #-----------------------------------------------------# 
        # Created empty list for storing pointers and values  #
        #-----------------------------------------------------#
        pointers = []
        values = []
        #---------------------------------------------------------------#
        # Count variable for counting the values in the set of B values #
        #---------------------------------------------------------------#
        count = 0
        #-------------------------------#
        # Started traversing the list   #
        #-------------------------------#
        while(current != None):
            # ---------------------------------------------------------------------------#
            # If count is less then B then append pointer to pointers and val to values  #
            # then increment the count and current                                       #
            #----------------------------------------------------------------------------#
            if count < B:
                pointers.append(current)
                values.append(current.val)
                current = current.next
                count += 1
            #----------------------------------------------------------------------------------------------------# 
            # If the set is full of B values then traverse pointers in forward order and values in reverse order #
            # Replace the value of pointers with new values                                                      #
            #----------------------------------------------------------------------------------------------------#
            else:
                for i in range(B):
                    element = pointers.pop(0)
                    element.val = values.pop(-1)
                count = 0
        #--------------------------------------------------------------------------------------#
        # This is to handle the last set or value after while loop end approching None pointer #
        #--------------------------------------------------------------------------------------#
        for i in range(B):
            element = pointers.pop(0)
            element.val = values.pop(-1)
        #-----------------# 
        # Return the Head #
        #-----------------#
        return(A)
        

