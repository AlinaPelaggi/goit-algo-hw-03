from datetime import datetime

def get_days_from_today(date: str) -> int:
    global date_user
    current_date = datetime.today().date()             #Поточна дата без урахування часу
    
    try:
        date_user = datetime.strptime(date_user, "%Y-%m-%d")
        days_user = datetime.toordinal(date_user) - datetime.toordinal(current_date)         #Рахуємо кількість днів між датами
        print(days_user)
        return days_user       #Функція має повернути кількість днів між датами
    except ValueError:
        print(f"ERROR  Date enterder wrong")
    except Exception: 
        pass

date_user = "2024-12-12"
get_days_from_today(date_user)
