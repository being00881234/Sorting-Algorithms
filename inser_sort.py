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


a=list()

inputs=int(input("No of elments to add:"))

for _ in range(inputs):
    a.append(int(input()))

#print(a)
print(insert_sort(a))