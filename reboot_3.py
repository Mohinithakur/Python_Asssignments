list = []
list1 =[]
list2 = []

n = int(input("Enter no.of elements : "))

#taking user input.
for i in range(0,n):
    elements = int(input())

    list.append(elements)
print(list)

print("Nos. greater than 5: ")
#only those numbers greater than 5
for i in range(0,n):
    if (list[i]>5):
        list1.append(list[i]) #storing the values in a list
    elif (list[i]<=2):
        list2.append(list[i])#storing value in a list
print("Nos. greater than 5:  ",list1)
print("Nos. less than 2:  ",list2)

        




