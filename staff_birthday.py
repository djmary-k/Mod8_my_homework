# Завдання
# Вам потрібно реалізувати корисну функцію для виведення списку колег, яких потрібно привітати з днем народження 
# на тижні.
# У вас є список словників users, кожен словник у ньому обов'язково має ключі name та birthday. 
# Така структура представляє модель списку користувачів з їх іменами та днями народження. name — це рядок 
# з ім'ям користувача, а birthday — це datetime об'єкт, в якому записаний день народження.
# Ваше завдання написати функцію get_birthdays_per_week, яка отримує на вхід список users і виводить у 
# консоль (за допомогою print) список користувачів, яких потрібно привітати по днях.

# Умови приймання
# get_birthdays_per_week виводить іменинників у форматі:
# Monday: Bill, Jill
# Friday: Kim, Jan

# Користувачів, у яких день народження був на вихідних, потрібно привітати в понеділок.
# Для тестування зручно створити тестовий список users та заповнити його самостійно.
# Функція виводить користувачів з днями народження на тиждень вперед від поточного дня.
# Тиждень починається з понеділка.

from datetime import datetime, date, timedelta
# import random

users = [
    {'name': 'Nick', 'birthday': datetime(1971, 8, 1)}, #Tuesday
    {'name': 'John', 'birthday': datetime(1990, 8, 3)}, #Thursday
    {'name': 'Hanna', 'birthday': datetime(1952, 8, 9)}, #Wednesday
    {'name': 'Greg', 'birthday': datetime(1983, 7, 29)}, #Saturday
    {'name': 'Mia', 'birthday': datetime(1984, 7, 30)}, #Sunday
    {'name': 'Mary', 'birthday': datetime(1989, 7, 31)}, #Monday
    {'name': 'Kate', 'birthday': datetime(1993, 8, 3)}, #Thursday
    {'name': 'Adam', 'birthday': datetime(1989, 8, 4)}, #Friday
    {'name': 'Joana', 'birthday': datetime(1989, 8, 5)}, #Saturday
    {'name': 'Chris', 'birthday': datetime(1989, 8, 3)}, #Thursday
    {'name': 'Susy', 'birthday': datetime(1989, 8, 6)}, #Sunday
    {'name': 'Sam', 'birthday': datetime(1989, 8, 1)}, #Tuesday

    # {'name': 'Kate2', 'birthday': datetime(1993, 8, 7)}, #Monday
    # {'name': 'Adam2', 'birthday': datetime(1989, 8, 8)}, #Tuesday
    # {'name': 'Joana2', 'birthday': datetime(1989, 8, 9)}, #Wednesday
    # {'name': 'Chris2', 'birthday': datetime(1989, 8, 10)}, #Thursday
    # {'name': 'Susy2', 'birthday': datetime(1989, 8, 11)}, #Friday
    # {'name': 'Sam2', 'birthday': datetime(1989, 8, 12)}, #Saturday
    ]

def get_birthdays_per_week(users):
    current_date = datetime.now()
    # current_date = datetime(2023, 8, 1)
    # current_date = datetime(2023, 7, 30)
    start_bd_week = current_date.date()
    # print(start_bd_week)
    end_bd_week = start_bd_week + timedelta(days=6)
    # print(end_bd_week)
    
    for i in range(7):
        searcher_monday = start_bd_week + timedelta(days=i)
        if searcher_monday.weekday() == 0:
            monday_date = searcher_monday
    # print(monday_date)

    Monday = []
    Tuesday = []
    Wednesday = []
    Thursday = []
    Friday = []

    for user in users:        
        user['birthday'] = user['birthday'].date().replace(year=datetime.now().year)        
        if start_bd_week <= user['birthday'] <= end_bd_week:
            if  user['birthday'].weekday() == 0:
                Monday.append(user['name'])
            elif user['birthday'].weekday() == 1:
                Tuesday.append(user['name'])
            elif user['birthday'].weekday() == 2:
                Wednesday.append(user['name'])
            elif user['birthday'].weekday() == 3:
                Thursday.append(user['name'])
            elif user['birthday'].weekday() == 4:
                Friday.append(user['name'])
            elif user['birthday'].weekday() == 5 and user['birthday'] < monday_date:
                Monday.append(user['name'])            
            elif user['birthday'].weekday() == 6 and user['birthday'] < monday_date:
                Monday.append(user['name'])
            

        
    if len(Monday) > 0:
        print(f'Monday: {", ".join(Monday)}')
    if len(Tuesday) > 0:
        print(f'Tuesday: {", ".join(Tuesday)}')
    if len(Wednesday) > 0:    
        print(f'Wednesday: {", ".join(Wednesday)}')
    if len(Thursday) > 0:
        print(f'Thursday: {", ".join(Thursday)}')
    if len(Friday) > 0:    
        print(f'Friday: {", ".join(Friday)}')

    return 


if __name__ == '__main__':
    get_birthdays_per_week(users)
