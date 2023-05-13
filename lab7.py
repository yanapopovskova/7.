"""Написать объектно-ориентированную реализацию.
В программе должны быть реализованы минимум один класс, три атрибута, два метода.

№12 Сгенерировать все возможные одномерные массивы из чисел 0, 1, 2 и 3, где сумма элементов массива должна быть равна 6.
Целевая функция заключается в генерации всех уникальных комбинаций, где сумма элементов равна 6."""

#Создаём класс Combinations
class Combinations:
    #Создаем конструктор класса.

    #Конструктор класса принимает два аргумента: n - количество элементов в комбинации,
    #sum_value - сумма элементов, которую должна давать комбинация.
    #Создаём три переменные: n, sum_value и combinations - список для хранения всех сгенерированных комбинаций.

    def __init__(self, n, sum_value):
        self.n = n
        self.sum_value = sum_value
        self.combinations = []

    def generate_combinations(self):  #Метод generate_combinations() генерирует все возможные комбинации из n элементов, которые в сумме дают значение sum_value.
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    for l in range(self.n):
                        if i != j and i != k and i != l and j != k and j != l and k != l:
                            if i + j + k + l == self.sum_value:
                                self.combinations.append([i, j, k, l])

    def print_combinations(self):   #Метод print_combinations(). Выводит на экран количество сгенерированных комбинаций и все сгенерированные комбинации.
        print("Количество комбинаций:", len(self.combinations))
        print("Все комбинации:")
        for combination in self.combinations:
            print(combination)

#Создаём объект класса Combinations с параметрами n=4 и sum_value=6.

combinations = Combinations(4, 6)
combinations.generate_combinations()
combinations.print_combinations()