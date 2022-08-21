def dynamicselectionSort(array, size):
   
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])


print('Gebe sie minimu 4 Ziffern ein: ')
zahlen = list(map(int, input().split()))
size = len(zahlen)
dynamicselectionSort(zahlen, size)
print('Sortierte Ausgabe')
print(zahlen)