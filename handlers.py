
from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message

from kb import groups
from kb import teachers
from datetime import datetime
import kb
import text
import zameni
from database import DataBase
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
router = Router()

import para

class UserState(StatesGroup):
    weekday = State()
    weekdays = State()


@router.message(Command("start"))
async def start_handler(msg: Message):
    photo = 'https://sun9-37.userapi.com/impg/QlvEe47gGtt_kEMUDxSxNB0r54xO1EfvwJtQPw/66kOHPB8HUc.jpg?size=1284x1160&quality=96&sign=c4cc6538e23aa90af846829d55e81247&type=album'
    p = DataBase
    p.add_user(msg.from_user.id, msg.from_user.first_name)
    await msg.answer_photo(photo = photo, caption = str(text.greet.format(name=msg.from_user.full_name)), reply_markup=kb.menu)



@router.callback_query(F.data == 'nextday')
@router.callback_query(F.data == 'prevday')
@router.callback_query(F.data == 'get_timetable')
async def change_timetable_day(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(UserState.weekday)
    tele_user_id = callback.from_user.id

    if callback.data == 'nextday':
        daynumber = await state.get_data()
        await state.update_data(weekday = daynumber['weekday'] + 1)
        daynumber = await state.get_data()

    elif callback.data == 'prevday':
        daynumber = await state.get_data()
        await state.update_data(weekday = daynumber['weekday'] - 1)
        daynumber = await state.get_data()

    elif callback.data == 'get_timetable':
        await state.update_data(weekday = datetime.isoweekday(datetime.now()))
        daynumber = await state.get_data()

    daynumber = int(daynumber['weekday'])
    
    if daynumber < 1 or daynumber > 6:
        await state.update_data(weekday = datetime.isoweekday(datetime.now()))

    if daynumber in [1, 7]:
        await callback.message.edit_caption(caption = para.get_timetable(1, tele_user_id), reply_markup=kb.timetable_monday)

    elif daynumber == 6:
        await callback.message.edit_caption(caption = para.get_timetable(daynumber, tele_user_id), reply_markup=kb.timetable_saturday)

    else:
        await callback.message.edit_caption(caption = para.get_timetable(daynumber, tele_user_id), reply_markup=kb.timetable.as_markup())




@router.callback_query(F.data == 'get_zameni')
async def change_timetable_day(callback: types.CallbackQuery):
    tele_user_id = callback.from_user.id
    await callback.message.edit_caption(caption = zameni.zameni_group(tele_user_id), reply_markup=kb.back)

@router.callback_query(F.data == 'home')
async def home(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_caption(caption = text.menu, reply_markup=kb.menu)

@router.callback_query(F.data == 'choose_group')
async def choose_group(callback: types.CallbackQuery):
    await callback.message.edit_caption(caption = text.choose_group.format(group = DataBase.get_group(callback.from_user.id)), reply_markup=kb.gbuilder.as_markup())

@router.callback_query(F.data == 'get_timetable_teacher')
async def get_teacher_timetable(callback: types.CallbackQuery):
    await callback.message.edit_caption(caption=text.choose_teacher, reply_markup=kb.tbuilder.as_markup())

@router.callback_query(F.data.in_(groups))
async def change_group(callback: types.CallbackQuery):
    p = DataBase
    p.change_group(callback.from_user.id, callback.data)
    await callback.message.edit_caption(caption = text.group_changed.format(group = callback.data), reply_markup=kb.back)

@router.callback_query(F.data.in_(teachers))
async def choose_teacher(callback: types.CallbackQuery):
    await callback.message.edit_caption(caption = text.teacher_timetable.format(teacher = callback.data), reply_markup=kb.back)