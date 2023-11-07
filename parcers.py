import requests
from pathlib import Path
import win32com.client as win32
from win32com.client import constants
import os
import re


class getFiles():
    def __init__(self) -> None:
        self.word = os.getcwd + "\\docs\\zameni.doc"
        self.excel = os.getcwd + "\\docs\\raspisanie.xls"

        self.download_docx()
        self.download_xlsx()

    def save_as_xlsx(self, path: Path) -> None:
        excel = win32.gencache.EnsureDispatch('Excel.Application')
        page = excel.Workbooks.Open(path)
        page.Activate ()

        # Rename path with .docx
        new_file_abs = os.path.abspath(path)
        new_file_abs = re.sub(r'\.\w+$', '.xlsx', new_file_abs)

        # Save and Close
        excel.ActiveWorkbook.SaveAs(
            new_file_abs, FileFormat=51
        )
        page.Close(False)

    def save_as_docx(self, path):
        word = win32.gencache.EnsureDispatch('Word.Application')
        doc = word.Documents.Open(path)
        doc.Activate ()

        # Rename path with .docx
        new_file_abs = os.path.abspath(path)
        new_file_abs = re.sub(r'\.\w+$', '.docx', new_file_abs)

        # Save and Close
        word.ActiveDocument.SaveAs(
            new_file_abs, FileFormat=constants.wdFormatXMLDocument
        )
        doc.Close(False)

    def download_docx(self):
        try:
            response = requests.get("https://vgpgk.ru/raspisanie/vgpgk-zameny-1-korpus.doc?v=2023011141816")

            with open('docs\\zameni.doc', 'wb') as file:
                file.write(response.content)

            self.save_as_docx(self.word)
        except:
            print("Ошибка парса расписания")
        
    def download_xlsx(self):
        try:
            response = requests.get("https://vgpgk.ru/raspisanie/1-korpus_1-smena_1-semestr_2022.xls?v=2023011141816")

            with open('docs\\raspisanie.xls', 'wb') as file:
                file.write(response.content)

            
            self.save_as_xlsx(self.excel)
        except:
            print("Ошибка парса замен")
        

