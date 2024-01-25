list=[1,2,2,3,3,4,5,6,7,7,8,9,9]
list2=[]
print("duplicates are:",end=' ')
for x in list:
    if x not in list2:
        list2.append(x)
        
    else:
        print(x, end=' ')

    
        


