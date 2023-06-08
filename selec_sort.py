    
def sel_sort(list2):
    for i in range(len(list2)
    ):
        min=i
        for j in range(i+1,len(list2)):
            if list2[j]<list2[min]:
                min=j
        list2[min],list2[i]=list2[i],list2[min]
    return(list2)

a=list()

inputs=int(input("No of elments to add:"))

for _ in range(inputs):
    a.append(int(input()))

print(sel_sort(a))