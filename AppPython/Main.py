import time
import random
from countSort import countsort
from quickSort import insertsort,quicksort
from bubbleSort import bubbleSort
from shellSort import shellSort
from verificare import verificareBubbleSort,verificareCountSort,verificareQuickSort,verificareShellSort
f = open("teste.in", "w")
nrlinii=int(input("Nrlinii="))
f.write(str(nrlinii))
f.write("\n")
def generarenumere(n):
    global L
    L=[]
    for i in range(n):
        st = ""
        l=[]

        for j in range(random.randrange(1000,3000)):
            x = str(random.randrange(1000000))
            l.append(int(x))
            st += x + ' '
        L.append(l)
        f.write(st)
        f.write('\n')
generarenumere(nrlinii)

for i in range (nrlinii):
    print("Sortarea facuta cu countsort:")
    start_time=time.time()
    print(countsort(L[i]))
    end_time=time.time()
    print(end_time-start_time)
    verificareCountSort(L[i])
    print("\n")
    print("Sortare facuta cu quicksort:")
    start_time=time.time()
    print(quicksort(L[i]))
    end_time=time.time()
    print(end_time-start_time)
    verificareQuickSort(L[i])
    print("\n")

    print("Sortare facuta cu bubblesort:")
    start_time = time.time()
    print(bubbleSort(L[i]))
    end_time = time.time()
    print(end_time - start_time)
    verificareBubbleSort(L[i])
    print("\n")

    print("Sortare facuta cu shellsort:")
    start_time = time.time()
    print(shellSort(L[i]))
    end_time = time.time()
    print(end_time - start_time)
    verificareShellSort(L[i])
    print("\n")

    print("Sortare facuta cu sort-ul din python:")
    start_time = time.time()
    print(sorted(L[i]))
    end_time = time.time()
    print(end_time - start_time)
    print("Sortare corecta")
    print("\n")