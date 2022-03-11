import time
import random
from countSort import countsort
from quickSort import insertsort,quicksort
from bubbleSort import bubbleSort
from shellSort import shellSort
from radixSort import radixSort
def verificareBubbleSort(arr):
    d=bubbleSort(arr)
    if d==sorted(arr):
        print("Sortare corecta")
    else:
        print("Sortare incorecta")

def verificareCountSort(arr):
    d=countsort(arr)
    if d==sorted(arr):
        print("Sortare corecta")
    else:
        print("Sortare incorecta")

def verificareQuickSort(arr):
    d=quicksort(arr)
    if d==sorted(arr):
        print("Sortare corecta")
    else:
        print("Sortare incorecta")

def verificareShellSort(arr):
    d = shellSort(arr)
    if d==sorted(arr):
        print("Sortare corecta")
    else:
        print("Sortare incorecta")

def verificareRadixSort(arr):
    d = radixSort(arr)
    if d == sorted(arr):
        print("Sortare corecta")
    else:
        print("Sortare incorecta")