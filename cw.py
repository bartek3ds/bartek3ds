from sys import getsizeof

lista = [1, 2, 3]
lista_15 = [i + 15 for i in lista]
print(lista_15)
string_lista = ['a', 'b', 'c', 'd']
napis = "-".join(string_lista)
print(napis)
tuple = (1, 2, 3)
print(getsizeof(lista))
print(getsizeof(tuple))


class Cat:
    def __init__(self, wiek, imie, cena):
        self.wiek = wiek
        self.imie = imie
        self.cena = cena

    def get_wiek(self):
        return self.wiek


kotek1 = Cat(10, 'Puszek', 100)
wiek = kotek1.get_wiek()
print(wiek)

napis1 = 'abcdefg'  # Czy znajduje się w danym ciągu
if 'a' in napis1:
    print("True")
if 'b' not in napis1:
    print("True")
else:
    print("False")

tuple = ()

y = [8, 2, 3]
for index, item in enumerate(y):  # numerowanie  + wartosc
    tuple += (index + 1, item)
print(tuple)

tuple = ('Kevin', 'Niklas', 'Jenny', 'Craig')  # najmniejsza wartosc slowa
print(min(tuple))

print(max(tuple))  # Największa wartość

y = (i for i in range(1, 100))
print(sum(y))  # Suma liczb
y = [8, 3, 2, 1]
print(sum(y[-2:]))  # Wybrany przedział

y_cp = y.copy()
print(sorted(y_cp))  # Sortowanie
napis = 'errors'
print(sorted(napis))  # Litery napisu posortowane

tuple = sorted(tuple, key=lambda k: k[1])  # Sortowanie po 2 literze alfabetu
print(tuple)

print(napis.count('r'))  # Licznik
print(napis.index('o'))  # Indeks pierwszej podanej zmiennej

y = ('cat', 'dog', 'cow')
cat, dog, cow = y  # Odpakowywanie z listy, tupli
print(cat, dog, cow)

y = [1, 2, 3, 4, 6]
del y[-1]  # Usuwa ostatni element listy
print(y)
del y  # Usuwa liste

y = [1, 2, 4, 5, 6]
y.insert(2, 3)  # Dodaje zmienna do wybranego przez nas indeksu
print(y)

ostatni = y.pop()  # Domyslne usuwa ostatni element ( wybor indeksu)
print(y)
print(ostatni)

y.remove(2)  # Usuwa pierwszą wpisaną zmienną

y.reverse()  # odwraca listę
print(y)
print(y[::-1])  # Odwraca listę

y = ['b', 'e', 'a']
y.sort()  # Sortowanie listy metodą list.sort()
print(y)

y.sort(reverse=True)  # Sortowanie malejąco
print(y)

x = {i for i in range(1, 10, 2)}
print(type(x))
y = (1, 3, 4, 5, 1, 4, 5, 2, 1)  # Zamiana tupli na seta
abc = set(y)
print(abc)

x.add(11)  # Dodawanie do seta
print(x)
x.remove(3)  # Odejmowanie wybranej zmiennej
print(x)

x.clear()  # Wyczyszcenie calego setu
print(x)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 & s2)  # wspolna część
print(s1 | s2)  # Razem
print(s1 ^ s2)  # Razem z wyjątkiem cżęsci wspolnej
print(s1 - s2)  # Lista1 bez elementow  zlisty 2
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5, 6}
print(s1 <= s2)
print(s1.issubset(s2))  # czy s1 zawiera się w s2
print(s2.issuperset(s1))  # czy s2 zawiera kazdy element z s1
print(s1 >= s2)

dictionary = {1: 'pork', 2: 'pork2', 3: 'pork3'}  # Tworzenie slownika
print(type(dictionary))
dictionary = dict(pork=1, pork2=3, pork3=4)
print(dictionary)

dictionary['pork'] = 2
print(dictionary['pork'])
print(dictionary.keys())  # Klucze slownika
print(dictionary.values())  # wartosci slownika
print(dictionary.items())  # zawartosc slownika (klucz + wartosc)

if 'pork2' in dictionary:  # Czy klucz sie znajduje
    print(dictionary['pork2'])
if 4 in dictionary.values():  # Czy wartosc sie znajduje
    print("pork")

for key in dictionary:  # Iterowanie w slowniku
    print(key, dictionary[key])
for k, v in dictionary.items():
    print(k, v)

import numpy as np

random_numbers = np.random.randint(1, 20, 3)  # Randomowe liczby
print(random_numbers)
tajnykod = 'I mean to Be here b3ut you is 2 to go while we can do it 1'
kod = [x for x in tajnykod if x.isnumeric()]  # jezeli jest wartoscia numeryczną    liczba.isnumeric()
kod = "".join(kod)
print(kod)

letters = [x for x in 'ABCDEFG']
np.random.shuffle(letters)  # randomow wymiesza
print(letters)
x_list = [x for x in range(1, 10)]
x_l = [x if x % 2 == 0 else x * 100 for x in x_list]
print(x_l)
a = [[1, 2, [3, 5]], [3, 4, [5, 4]]]
y = [x for b in a for x in b]
print(y)


# Stos
class Stack:
    def __init__(self):
        self.stack = list()  # Pusty stos

    def push(self, item):  # Dodanie elementu na szczyt
        self.stack.append(item)

    def pop(self):  # usuniecie elementu ze szczytu
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def peek(self):  # sprawdzenie jaki element jest na szczycie
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None

    def __str__(self):  # Zwrocenie stosu jako ciagu znakow
        return str(self.stack)


my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
print(my_stack)
print(my_stack.pop())
print(my_stack.peek())
print(my_stack.__str__())

from collections import deque  # Metoda dodajaja lub usuwajaca elementy ( z lewej lub z prawej strony)

my_queue = deque()
my_queue.append(5)
my_queue.append(10)
print(my_queue)
print(my_queue.popleft())  # Pieerwsze z lewej


# Max Heap

class MaxHeap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)

    def __str__(self):
        return str(self.heap)


mx = MaxHeap([1, 2, 3, 4, 5])
mx.push(10)
mx.push(4)
mx.push(100)
print(mx)
x, y = 1, 2
x, y = y, x  # Zamiana
print(x, y)


class Node:
    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p

    def __str__(self):
        return '(' + str(self.data) + ')'


class LinkedList:
    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            else:
                this_node = this_node.next_node
        return None

    def remove(self, d):
        this_node = self.root
        prev_node = None

        while this_node is not None:
            if this_node.data == d:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    self.root = this_node.next_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False
    def print_list(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end='->')
            this_node = this_node.next_node
        print('None')

list1 = LinkedList()
list1.add(5)
list1.add(10)
list1.add(15)
list1.print_list()

print(list1.size)
print(list1.find(11))
list1.remove(5)
list1.print_list()
