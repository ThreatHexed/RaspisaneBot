
from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message

from kb import groups
from kb import teachers
import kb
import text
from database import DataBase
router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    photo = 'https://sun9-37.userapi.com/impg/QlvEe47gGtt_kEMUDxSxNB0r54xO1EfvwJtQPw/66kOHPB8HUc.jpg?size=1284x1160&quality=96&sign=c4cc6538e23aa90af846829d55e81247&type=album'
    p = DataBase
    p.add_user(msg.from_user.id)
    await msg.answer_photo(photo = photo, caption = str(text.greet.format(name=msg.from_user.full_name)), reply_markup=kb.menu)


@router.callback_query(F.data == 'get_schedule')
async def get_shelude(callback: types.CallbackQuery):
    await callback.message.edit_caption(caption = text.shelude, reply_markup=kb.back)

@router.callback_query(F.data == 'home')
async def home(callback: types.CallbackQuery):
    await callback.message.edit_caption(caption = text.menu, reply_markup=kb.menu)

@router.callback_query(F.data == 'choose_group')
async def choose_group(callback: types.CallbackQuery):
    await callback.message.edit_caption(caption = text.choose_group.format(group = DataBase.get_group(callback.from_user.id)), reply_markup=kb.gbuilder.as_markup())

@router.callback_query(F.data == 'get_shelude_teacher')
async def get_teacher_shelude(callback: types.CallbackQuery):
    await callback.message.edit_caption(caption=text.choose_teacher, reply_markup=kb.tbuilder.as_markup())

@router.callback_query()
async def change_group(callback: types.CallbackQuery):
    if callback.data in groups:
        p = DataBase
        p.change_group(callback.from_user.id, callback.data)
        await callback.message.edit_caption(caption = text.group_changed.format(group = callback.data), reply_markup=kb.back)
    if callback.data in teachers:
        await callback.message.edit_caption(caption = text.teacher_shelude.format(teacher = callback.data), reply_markup=kb.back)