from datetime import datetime

def get_days_from_today():
    current_date = datetime.today()               #Поточна дата без урахування часу
           
    #ЦИКЛ перевірки введеної дати користувачем (нескінченний цикл)
    while True:
        date_user = input('Enter the date:  ')
        try:
            date_user = datetime.strptime(date_user, "%Y-%m-%d")
            count_days = datetime.toordinal(date_user) - datetime.toordinal(current_date)         #Рахуємо кількість днів між датами
            break
        except Exception:
            print(f"ERROR! try again")
            
    #Функція має повернути кількість днів між датами 
    return count_days
