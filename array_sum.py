def find_sub_array(l, val):
    
    for i in range(len(l)-1 ):
        s=l[i]
        indexes = [i]
        
        for j in range(i+1, len(l)):
            
            s+= l[j]
            if abs(l[indexes[-1]] - l[j]) == 1:
                indexes.append(j)
            else:
                break
                
            if s==val:
                return indexes
        
    return [-1,-1]
    
l=[int(i) for i in input('Enter elements to list:: ').split(',')]
val=int(input('Enter an Value:: '))

find_sub_array(l, val)
