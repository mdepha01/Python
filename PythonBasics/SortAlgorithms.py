# sort algorithms

# selection sort algorithm
def selection(list):
    print(len(list))
    for i in range(0, len(list)):
        min = i
        for j in range(i+1, len(list)):
            if list[j] < list[min]:
                min = j
        list[i], list[min] = list[min], list[i]

list = [20,30,2,7,5]
#selection(list)
#print(list)

# bubble sort algorithm
def bubblesort(list):
    for i in range (0, len(list)):
        for j in range (i+1, len(list)):
            if list[j] < list[i]:
                list[i], list[j] = list[j], list[i]

#bubblesort(list)
#print(list
# insertion sort
def insertsort(list):
    for i in range (1, len(list)):
        temp = list[i]
        j = i-1
        while j >= 0 and list[j] > temp:
            list[j+1] = list[j]    # shift
            j -= 1
        list[j+1] = temp
insertsort(list)
print(list)
