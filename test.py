

import docx

def parse_word(filename):
    # Открываем документ Word
    word_doc = docx.Document(filename)

    # Создаем словарь для хранения замен
    replacements = {}

    # Проходим по параграфам документа
    for paragraph in word_doc.paragraphs:
        # Если параграф начинается с заголовка "Замены", то начинаем парсить
        if paragraph.text.startswith("Замены"):
            # Создаем словарь для хранения замен для текущей группы
            group = paragraph.text.split(" ")[1]
            replacements[group] = {}

        # Если параграф содержит замену, то добавляем ее в словарь
        for run in paragraph.runs:
            if "Группа" in run.text:
                # Получаем номер группы
                group = run.text.split(" ")[1]

                # Получаем название предмета
                subject = run.text.split(" ")[2]

                # Получаем преподавателя
                teacher = run.text.split(" ")[3]

                # Добавляем замену в словарь
                replacements[group][subject] = teacher

    return replacements

# Получаем имя файла Word
filename = "zameni.docx"

# Парсим замены
replacements = parse_word(filename)

# Выводим замены для группы ИБ-201
print(replacements)