#Третє завдання
import re

def normalize_phone(phone_number: str) -> str:
    global raw_numbers
    pattern = r"[;,\-:!\. ()/\\t\\n]"                         
    replacement = "" 
    formatted = re.sub(pattern, replacement, phone_number)

    pattern2 = '38'      
    pattern3 = '+'
    if pattern2 not in phone_number:
        formatted = pattern2 + formatted
    if pattern3 not in phone_number:
        formatted = pattern3 + formatted
    
    return formatted


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:\n", sanitized_numbers)