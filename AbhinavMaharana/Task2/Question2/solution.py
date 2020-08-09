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

