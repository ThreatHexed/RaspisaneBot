from urllib import request
import requests
import aspose.words as aw
import time
from xls2xlsx import XLS2XLSX

def download():

    try:
        response = requests.get('https://vgpgk.ru/raspisanie/1-korpus_1-smena_1-semestr_2022.xls?v=2023011141816')

        with open('raspisanie.xls', 'wb') as file:
            file.write(response.content) 

        x2x = XLS2XLSX('raspisanie.xls')
        x2x.to_xlsx('raspisanie.xlsx')

    except Exception as ex:
        return 'Что-то пошло не так'
    
    try:
        response = requests.get('https://vgpgk.ru/raspisanie/vgpgk-zameny-1-korpus.doc?v=2023011141816')

        with open('zameni.doc', 'wb') as file:
            file.write(response.content)
        
        doc = aw.Document('zameni.doc')
        doc.save('zameni.docx')

    except Exception as ex:
        return 'Что-то пошло не так'
    
while True:
    print(download())
    print("закачал")
    time.sleep(900)
