
print("Wählen Sie die Option: Die [1] sortiert die Zahlen aufsteigend und die [2] absteigend")
userInput  = input()

def dynamicBubbleSort(list):
    
    if userInput == "1":
        print('Aufsteigend sortiert:')
        for i in range(len(list)):
            for j in range(0, len(list) - i - 1):
                if list[j] > list[j +1]:
                    temp = list[j]
                    list[j] = list[j + 1]
                    list[j + 1] = temp
    elif userInput == "2":
        print('Absteigend sortiert:')
        for i in range(len(list)):
            for j in range(0, len(list) - i - 1):
                if list[j] < list[j +1]:
                    temp = list[j]
                    list[j] = list[j + 1]
                    list[j + 1] = temp
    else:
        print("Falsche Eingabe.")


print('Gebe sie minimu 4 Ziffern ein: ')
zahlen = list(map(int, input().split()))

dynamicBubbleSort(zahlen)

print(zahlen)


