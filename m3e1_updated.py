from datetime import datetime

def get_days_from_today(date: str) -> int:
        current_date = datetime.today().date()             #Поточна дата без урахування часу
    
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
        days = datetime.toordinal(date) - datetime.toordinal(current_date)         #Рахуємо кількість днів між датами
        print(days)
        
    except ValueError:
        print(f"ERROR  Date enterder wrong")
    except Exception: 
        pass

    return days       #Функція має повернути кількість днів між датами

get_days_from_today("2024-12-20")
