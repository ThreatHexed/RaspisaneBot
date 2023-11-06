from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder

menu = [
    [InlineKeyboardButton(text="Расписание", callback_data='get_schedule')],
    [InlineKeyboardButton(text="Препод", callback_data="get_shelude_teacher")],
    [InlineKeyboardButton(text="Указать группу", callback_data='choose_group')]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)

back = [[InlineKeyboardButton(text="Назад🏠", callback_data='home')]]
back = InlineKeyboardMarkup(inline_keyboard=back)


groups = ['ИБ-201', 'ИБ-202', 'ИБ-211', 'ИБ-221', 'ИС-211', 'ИС-212', 'ИС-213💩', 'ИС-214', 'ИС-221', 'ИС-222', 'ИС-223', 'ИС-224', 'ИС-225', 'КК-201', 'КК-211', 'КК-212', 'КК-221', 'Я передумал🤨']

gbuilder = InlineKeyboardBuilder()
for i in groups:
    if "Я передумал" in i:
        gbuilder.button(text = i, callback_data = 'home')
    else:
        gbuilder.button(text = i, callback_data = i)

gbuilder.adjust(4,4,4,5,1)

teachers = ["Колесников", 'Я передумал🤨']
tbuilder = InlineKeyboardBuilder()
for i in teachers:
    if "Я передумал" in i:
        tbuilder.button(text = i, callback_data = 'home')
    else:
        tbuilder.button(text = i, callback_data = i)

tbuilder.adjust(1, 1)
