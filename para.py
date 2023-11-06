import pandas as pd
import json
from datetime import date
from datetime import datetime


def para_prepod(prepod):

    try:

        weekday = ['0', "Понедельник", "Вторник", "Среда", "Четверг",
                   "Пятница", "Суббота", "Понедельник", "Понедельник"]

        if datetime.now().hour > 8:
            userdate = str(date.today().isoweekday()+1)

        else:
            userdate = str(date.today().isoweekday())

        with open("2.json", "r", encoding='utf-8') as f:
            data = json.load(f)

        day = data[userdate]

        excel = pd.read_excel(io='test1.xlsx',
            engine='openpyxl',
            usecols='A:S',
            header=8,
            )

        para = f'{weekday[int(userdate)]}\n\n'

        for id, day_number in enumerate(day, 2):
            hui = False
            for group in excel:
                
                if str(excel[group].loc[day[day_number]]).find(str(prepod)) > -1 and hui == False:
                    hui = True
                    para += (f"____________\n{excel[group].loc[0]} \n {excel[group].loc[day[day_number]-1]} \n {excel[group].loc[day[day_number]]}\n")

                elif str(excel[group].loc[day[day_number]]).find(str(prepod)) > -1 and hui == True:
                    para += (f"{excel[group].loc[0]} \n {excel[group].loc[day[day_number]-1]} \n {excel[group].loc[day[day_number]]}\n")

        if prepod == 'Колесников':
            para += "\nТакого преподавателя я в хуй не дул, и вообще, дядя, кто ты нахуй такой"
        print(para)
        return para
    except Exception as e:
        return f"Ошибки \n {e} \n А теперь пиздуй чинить"
    

def raspisanie_students(group):
    try:

        day228 = ['0', "Понедельник", "Вторник", "Среда", "Четверг",
                "Пятница", "Суббота", "Понедельник", "Понедельник"]
        if datetime.now().hour > 12:
            date1 = str(date.today().isoweekday()+1)
            date2 = int(date.today().isoweekday()+1)
        else:
            date1 = str(date.today().isoweekday())
            date2 = int(date.today().isoweekday())

        with open("1.json", "r", encoding='utf-8') as f:
            data = json.load(f)

        raspisanie = f'{day228[date2]}\n'
        day = data[date1]
        text = pd.read_excel(io='test1.xlsx',
                            engine='openpyxl',
                            usecols='A:S',
                            header=9,
                            )
        text = text.fillna("Пары нет")
        for id, i in enumerate(day, 2):
            day1 = int(day[i])
            if id % 2 == 0:
                id -= int(id/2)
            else:
                id = ""
            raspisanie += f'\n{str(id)} {str(text[group].loc[day1])}'
        return raspisanie
    except Exception as e:
        return f"Ошибки \n {e} \n А теперь пиздуй чинить"