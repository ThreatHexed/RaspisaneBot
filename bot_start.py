import asyncio
import logging
import threading
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
import bot_config
from bot_handlers import router, down

class BOT():
    async def check(self):
        while True:
            down.start()
            await asyncio.sleep(600)

    async def main(self):
        dp = Dispatcher(storage=MemoryStorage())
        bot = Bot(token=bot_config.BOT_TOKEN, parse_mode=ParseMode.HTML)
        dp.include_router(router)
        loop = asyncio.get_running_loop()

        chk = loop.create_task(self.check())

        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":    
    logging.basicConfig(level=logging.INFO)
    p = BOT()
    asyncio.run(p.main())
    
