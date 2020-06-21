def insertionSort(arr):

    for i in range(1, len(arr)):

        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key


input_array=list(map(int,input("Enter the values you need to sort my friend\n").split()))
insertionSort(input_array)
print("Sorted values are:",*input_array)
