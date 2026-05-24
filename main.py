import asyncio
import random
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = '8684676356:AAFn3L9uhbGqHymJzanCFmTvDnBVWZKklLQ'

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Списки фраз
bad_words = ['сука', 'бля', 'пидор', 'дебил', 'блят', 'блять', 'пошёл', 'ублюдок']
insult_replies = [
    "🎭 НУ И НУ! ПОВЕРЬ, ОНИ ТЕБЕ НИЧЕМ НЕ ПОМОГУТ. ПОМОЧЬ СЕБЕ МОЖЕШЬ ТОЛЬКО ТЫ.",
    "🎭 Ай-яй-яй, тебя уже учили, что нельзя материться! А ты! НУ ХОТЯ МНЕ РАЗРЕШАЮТ ВСЁ, ПОКА ТЕБЯ НЕТ.",
    "🎭 Ну и ну, как не стыдно! ДАЖЕ Я ТАК НЕ ДЕЛАЮ. Ведь это противно.",
    "🎭 Ублюдок? Какое низкое слово для столь ничтожного существа, как ты."
]

# Обработка матов (самая первая в списке)
@dp.message(F.text.lower().contains(tuple(bad_words)))
async def handle_bad_words(message: Message):
    await message.answer(random.choice(insult_replies))

# Остальные команды
@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("🎭 Шамиль (Шадоу Милк) НА СЦЕНЕ. ГОТОВЫ ЛИ ВЫ К ДРАМЕ?")

@dp.message(Command("joke"))
async def joke(message: Message):
    await message.answer("🎭 ЗНАЕШЬ КАКОЕ САМОЕ ЛОХОНУТОЕ СОЗДАНИЕ? ВЕРНО, ТЫ!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
