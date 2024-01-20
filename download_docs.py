import requests
import aspose.words as aw
import time
from xls2xlsx import XLS2XLSX
import os
import hashlib
from get_shelude import Shelude
from get_replacements import Replacement


class Docs(Shelude, Replacement):
    
    def __init__(self) -> None:
        self.path = os.getcwd()
        self.url_xls = 'https://vgpgk.ru/raspisanie/1-korpus_1-smena_1-semestr_2022.xls?v=2023011141816'
        self.url_doc = 'https://vgpgk.ru/raspisanie/vgpgk-zameny-1-korpus.doc?v=2023011141816'
        response_xls = requests.get(self.url_xls)
        response_doc = requests.get(self.url_doc)

        with open(self.path + r'/documents/raspisanie.xls', 'wb') as file:
            file.write(response_xls.content)
        print('[Status] XLS file is downloaded')

        x2x = XLS2XLSX(self.path + r'/documents/raspisanie.xls')
        x2x.to_xlsx(self.path + r'/documents/raspisanie.xlsx')
        print('[Status] XLS file converted to XLSX')


        with open(self.path + r'/documents/zameni.doc', 'wb') as file:
            file.write(response_doc.content)
        print('[Status] DOC file is downloaded')
        
        doc = aw.Document(self.path + r'/documents/zameni.doc')
        doc.save(self.path + r'/documents/zameni.docx')
        print('[Status] DOC file converted to DOCX')

        self.update_hash_xls()
        self.update_hash_doc()
        print('[Status] Initialization done!')
    # Обновляем хеш старых файлов
    def update_hash_xls(self):
        with open(self.path + r'/documents/raspisanie.xls', 'rb') as file:
            self.hash_main_xls = hashlib.sha256(str(file.read()).encode())
        print("[Status] XLS file hash updated")
        self.update_shelude()

    def update_hash_doc(self):
        with open(self.path + r'/documents/zameni.doc', 'rb') as file:
            self.hash_main_doc = hashlib.sha256(str(file.read()).encode())
        print("[Status] DOC file hash updated")
        self.update_replacement()

    
    # Сверяем хэш старых и новых файлов
    def check_hash_xls(self):
        
        response = requests.get(self.url_xls)
        self.hash_new_xls = hashlib.sha256(str(response.content).encode())
        if self.hash_main_xls.hexdigest() != self.hash_new_xls.hexdigest():
            print('[Status] New XLS file found')
            self.download_xls(response)

        else:
            print('[Status] XLS file hash sums are same, nothing to do')

    def check_hash_doc(self):
        response = requests.get(self.url_doc)
        self.hash_new_doc = hashlib.sha256(str(response.content).encode())
        if self.hash_main_doc.hexdigest() != self.hash_new_doc.hexdigest():
            print('[Status] New DOC file found')
            self.download_doc(response)
        else:
            print('[Status] DOC hash sums are same, nothing to do')

    # Скачиваем файлы
    def download_xls(self, response):
        with open(self.path + r'/documents/raspisanie.xls', 'wb') as file:
            file.write(response.content)
        print('[Status] new XLS file dowloaded')
        x2x = XLS2XLSX(self.path + r'/documents/raspisanie.xls')
        x2x.to_xlsx(self.path + r'/documents/raspisanie.xlsx')
        print('[Status] XLS file converted to XLSX')

        self.update_hash_xls()
    
    def download_doc(self, response):
        with open(self.path + r'/documents/zameni.doc', 'wb') as file:
            file.write(response.content)
        print('[Status] new DOC file dowloaded')
        doc = aw.Document(self.path + r'/documents/zameni.doc')
        doc.save(self.path + r'/documents/zameni.docx')
        print('[Status] DOC file converted to DOCX')

        self.update_hash_doc()


p = Docs()
while True:
            p.check_hash_xls()
            p.check_hash_doc()
            time.sleep(300)