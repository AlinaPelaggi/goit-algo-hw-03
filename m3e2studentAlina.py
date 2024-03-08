#Друге завдання
#Вам необхідно написати функцію get_numbers_ticket(min, max, quantity)
#яка допоможе генерувати набір унікальних випадкових чисел для лотерей.

import random

def get_numbers_ticket(min, max, quantity):
    #Перевіряємо чи параметри функції є правильними
    if min < 1 or max > 1000 or quantity > max - min: 
        return([])
        #Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список.
    else:
        #Функція генерує вказану кількість унікальних чисел у заданому діапазоні.                             
        list = [i for i in range (min, max + 1)]  
        #Функція повертає список випадково вибраних, відсортованих чисел.       
        random_numbers = random.sample(list, quantity)
        random_numbers.sort()                                
        return random_numbers
    
#Введення параметрів функції
min = int(input("Введіть мінімальне можливе число у наборі (не менше 1):"))
max = int(input("Введіть максимальне можливе число у наборі (не більше 1000):"))
quantity = int(input("Введіть кількість чисел, які потрібно вибрати:"))


print(get_numbers_ticket(min, max, quantity))
