def bubblesort(list2):
    n=len(list2)
    for i in range(n):
        for j in range(0,n-i-1):
            if list2[j]>list2[j+1]:
                 list2[j],list2[j+1]=list2[j+1],list2[j]
    return list2


a=list()

inputs=int(input("No of elments to add:"))

for _ in range(inputs):
    a.append(int(input()))

bubblesort(a)