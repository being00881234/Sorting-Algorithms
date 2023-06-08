def insert_sort(list3):
    for i in range (1,len(list3)):
        key=list3[i]
        j=i-1
        while j>=0 and key< list3[j]:
            list3[j+1]= list3[j]
            j=j-1
        else:
            list3[j+1]=key
    return(list3)


a=[15,6,13,22,3,52,2]
print(insert_sort(a))