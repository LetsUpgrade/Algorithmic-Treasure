def remove_duplicate(n,arr):

# the length of array should be gretaer than 1
# else return n 
    if n <= 1: 
        return n 
#temporary variable to store unique elements of the array  
    temp = list(range(n))

#transverse through the array 
    y = 0; 
    for x in range(0, n-1):

#if the present element is not equal to the incremented element
#then store the present element in temporary list and
#increment the j value
        if arr[x] != arr[x+1]: 
            temp[y] = arr[x] 
            y += 1
#also store the last element,since it was not stored previously 
    temp[y] = arr[n-1] 
    y += 1
#change the original array with unique elements and return j
    for x in range(0, y): 
        arr[x] = temp[x] 
  
    return y 

#Drivers code

arr = [1,2,2,4,5,7]
n=len(arr)
print( remove_duplicate(n,arr))

    

