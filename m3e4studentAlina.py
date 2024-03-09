#Четверте завдання
from datetime import datetime, timedelta 

#Список користувачів з їхніми датами народження
users = [  
    {"name": "NEXT FEB", "birthday": "1985.02.01"},
    {"name": "FUTURE", "birthday": "1990.03.27"},
    {"name": "Неділя", "birthday": "1990.03.10"},
    {"name": "Субота", "birthday": "1990.03.09"},
    {"name": "Минулий понеділок", "birthday": "1990.03.04"},
    {"name": "Майбутнє 1", "birthday": "1990.03.13"},
    {"name": "Майбутнє 2", "birthday": "1990.03.15"},
    {"name": "Дата з помилкою", "birthday": "190.03.12"},
    {"name": "NEXT JAN", "birthday": "1990.01.17"}
    ]

#Функцію get_upcoming_birthdays, яка допоможе вам визначати, кого з колег потрібно привітати.
def get_upcoming_birthdays(users):
    prepared_users = []         #Конвертований список з датю народження (із рядка у datetime).
    upcoming_birthdays = []     #Список майбутніх днів народження  
    nextyear_bithday = []       #Список днів народження на наступний рік
    days = 7                    #Кількість днів для перевірки на наближені дні народження
    today = datetime.today().date()  #Поточна дата


    # Функція для знаходження наступного заданого дня тижня після заданої дати
    def find_next_weekday(data, weekday: int):  
        days_ahead = weekday - data.weekday()       #Різниця між заданим днем тижня та днем тижня заданої дати
        if days_ahead <= 0:                         #Якщо день народження вже минув
                days_ahead += 7                     #Додаємо 7 днів, щоб отримати наступний тиждень
        return data + timedelta(days = days_ahead)  #Повертаємо нову дату

#1. Ви повинні перетворити дати народження з рядків у об'єкти datetime
    for user in users:          #Користувачеві зі списку
        try:
            birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()       #Конвертує рядок у у datetime
            prepared_users.append({"name": user['name'], 'birthday': birthday})     #Додаємо користувача з датою народження у форматі datetime до списку
        except ValueError:
            print(f'Некоректна дата народження для користувача {user["name"]}')     #Виводимо повідомлення про помилку
    
#3 & 4 Пройдіться по списку users. Перевірте, чи вже минув день народження в цьому році
    for user in prepared_users:  # Ітерація по підготовленим користувачам
        birthday_this_year = user["birthday"].replace(year=today.year)  # Заміна року на поточний для дня народження цього року
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)                #Замінемо у даті рік на наступний
            nextyear_bithday.append({"name": user['name'], 'birthday': birthday_this_year})     #Додаємо користувача до списку на наступний рік

#Актуальність та коректність визначення днів народження на 7 днів вперед.
        if 0 <= (birthday_this_year - today).days <= days:                                      #Якщо день народження в межах вказаного періоду
            if birthday_this_year.weekday() >= 5:                                               #Якщо день народження випадає на суботу або неділю
                birthday_this_year = find_next_weekday(birthday_this_year, 0)                   #Знаходимо наступний понеділок

            congratulation_date_str = birthday_this_year.strftime('%Y.%m.%d')                   #Форматуємо дату у рядок
            upcoming_birthdays.append({                                                         #Додаємо дані про майбутній день народження
                "name": user["name"],
                "congratulation_date": congratulation_date_str
            })
        elif (birthday_this_year - today).days > days:                                             #Пропускаємо майбутні дні народження
            pass

    return upcoming_birthdays

#Виклик функії get_upcoming_birthdays
print("Список привітань на цьому тижні:", get_upcoming_birthdays(users))