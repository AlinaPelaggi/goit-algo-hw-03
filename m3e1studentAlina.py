from datetime import datetime

def get_days_from_today(date):
    current_date = datetime.today()                                                                #Поточна дата без урахування часу
    days = datetime.toordinal(date) - datetime.toordinal(current_date)                             #Рахуємо кількість днів між датами
    
    return f'між Вашою датою {date_user.strftime("%d.%m.%Y")} та {current_date.strftime("%d.%m.%Y")} кількість днів становить {days}.'
    #функція поверне повідомлення для користувача

#ЦИКЛ перевірки введеної дати користувачем (нескінченний цикл)
while True:
    try:
        date_user = input("Введіть дату обчислення формату Рік.Місяць.День через крапку:    ")            
        date_user =  datetime.strptime(date_user, "%Y.%m.%d")
        break   
    except Exception:
        print(f"ERROR  Уважно ще раз введіть дату ЧЕРЕЗ КРАПКУ РІК.МІСЯЦЬ.ДЕНЬ (наприклад 2024.01.01)")

print(get_days_from_today(date_user))

    
