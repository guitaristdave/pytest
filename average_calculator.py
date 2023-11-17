class AverageCalculator:
    def calculate_average(self, numbers):
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)

def compare_averages(list1, list2):
    calculator = AverageCalculator()
    average1 = calculator.calculate_average(list1)
    average2 = calculator.calculate_average(list2)

    if average1 > average2:
        return "Первый список имеет большее среднее значение"
    elif average2 > average1:
        return "Второй список имеет большее среднее значение"
    else:
        return "Средние значения равны"


list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]
result = compare_averages(list1, list2)
print(result)
