from datetime import datetime
date_user = str

def get_days_from_today(date: str) -> int:
    current_date = datetime.today()               #Поточна дата без урахування часу
#ЦИКЛ перевірки введеної дати користувачем (нескінченний цикл)
    while True:
        date = input("Введіть дату обчислення:    ")
        try:
            date = datetime.strptime(date, "%Y-%m-%d")
            days = datetime.toordinal(date) - datetime.toordinal(current_date)         #Рахуємо кількість днів між датами
            break   
        except Exception:
            print(f"ERROR  Уважно ще раз введіть дату")
    
#Функція має повернути кількість днів між датами 
    return days

print(get_days_from_today(date_user))