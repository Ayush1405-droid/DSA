import array as arr

arr = arr.array('i' , [1,2,3,4,5,6,7,8,9])

ind = arr.index(8)

for i in range(0,len(arr)):
    print(ind[i], end=" ")


