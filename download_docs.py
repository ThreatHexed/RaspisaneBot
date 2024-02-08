import requests
import aspose.words as aw
from xls2xlsx import XLS2XLSX
import os
import hashlib
from get_shelude import Shelude
from get_replacements import Replacement
import asyncio
from datetime import datetime
import pytz
import time

def get_time():
    tz = pytz.timezone('Europe/Moscow')
    return datetime.now(tz).time().strftime("%H:%M:%S")


class Docs(Shelude, Replacement):
    def __init__(self) -> None:
        self.path = os.getcwd()
        print(self.path)
        self.url_xls = 'https://vgpgk.ru/raspisanie/1-korpus_1-smena_1-semestr_2022.xls?v=2023011141816'
        self.url_doc = 'https://vgpgk.ru/raspisanie/vgpgk-zameny-1-korpus.doc?v=2023011141816'
        response_xls = requests.get(self.url_xls)
        response_doc = requests.get(self.url_doc)


        if not os.path.isfile(self.path + r'/documents/raspisanie.xls'):
            with open(self.path + r'/documents/raspisanie.xls', 'wb') as file:
                file.write(response_xls.content)
            print(f'[{get_time()}][Status] XLS file is downloaded')

            if not os.path.isfile(self.path + r'/documents/raspisanie.xlsx'):
                x2x = XLS2XLSX(self.path + r'/documents/raspisanie.xls')
                x2x.to_xlsx(self.path + r'/documents/raspisanie.xlsx')
                print(f'[{get_time()}][Status] XLS file converted to XLSX')
            else:
                pass
        else:
            self.update_hash_xls()
            self.check_hash_xls()

        if not os.path.isfile(self.path + r'/documents/zameni.doc'):
            with open(self.path + r'/documents/zameni.doc', 'wb') as file:
                file.write(response_doc.content)
            print(f'[{get_time()}][Status] DOC file is downloaded')

            if not os.path.isfile(self.path + r'/documents/zameni.docx'):
                doc = aw.Document(self.path + r'/documents/zameni.doc')
                doc.save(self.path + r'/documents/zameni.docx')
                print(f'[{get_time()}][Status] DOC file converted to DOCX')
            else: pass
        else:
            self.update_hash_doc()
            self.check_hash_doc()

        

        self.update_hash_xls()
        self.update_hash_doc()
        print(f'[{get_time()}][Status] Initialization done!')
    # Обновляем хеш старых файлов
    def update_hash_xls(self):
        with open(self.path + r'/documents/raspisanie.xls', 'rb') as file:
            self.hash_main_xls = hashlib.sha256(str(file.read()).encode())
        print(f'[{get_time()}][Status] XLS file hash updated')
        self.shel_event.set()

    def update_hash_doc(self):
        with open(self.path + r'/documents/zameni.doc', 'rb') as file:
            self.hash_main_doc = hashlib.sha256(str(file.read()).encode())
        print(f'[{get_time()}][Status] DOC file hash updated')
        self.repl_event.set()

    
    # Сверяем хэш старых и новых файлов
    def check_hash_xls(self):
        
        response = requests.get(self.url_xls)
        self.hash_new_xls = hashlib.sha256(str(response.content).encode())
        if self.hash_main_xls.hexdigest() != self.hash_new_xls.hexdigest():
            print(f'[{get_time()}][Status] New XLS file found')
            self.download_xls(response)

        else:
            print(f'[{get_time()}][Status] XLS file hash sums are same, nothing to do')

    def check_hash_doc(self):
        response = requests.get(self.url_doc)
        self.hash_new_doc = hashlib.sha256(str(response.content).encode())
        if self.hash_main_doc.hexdigest() != self.hash_new_doc.hexdigest():
            print(f'[{get_time()}][Status] New DOC file found')
            self.download_doc(response)
        else:
            print(f'[{get_time()}][Status] DOC hash sums are same, nothing to do')

    # Скачиваем файлы
    def download_xls(self, response):
        with open(self.path + r'/documents/raspisanie.xls', 'wb') as file:
            file.write(response.content)
        print(f'[{get_time()}][Status] new XLS file dowloaded')
        x2x = XLS2XLSX(self.path + r'/documents/raspisanie.xls')
        x2x.to_xlsx(self.path + r'/documents/raspisanie.xlsx')
        print(f'[{get_time()}][Status] XLS file converted to XLSX')

        # self.update_hash_xls()
    
    def download_doc(self, response):
        with open(self.path + r'/documents/zameni.doc', 'wb') as file:
            file.write(response.content)
        print(f'[{get_time()}][Status] new DOC file dowloaded')
        doc = aw.Document(self.path + r'/documents/zameni.doc')
        doc.save(self.path + r'/documents/zameni.docx')
        print(f'[{get_time()}][Status] DOC file converted to DOCX')

            # self.update_hash_doc()
        # if True:
        #     download_doc(self, response_doc)
        #     download_xls(self, response_xls)
    def start(self):
        self.check_hash_xls()
        self.check_hash_doc()
                

