
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
        

