import asyncio
import random
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

# Твой токен
TOKEN = '8684676356:AAFn3L9uhbGqHymJzanCFmTvDnBVWZKklLQ'

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ID твоих стикеров
STICKER_ANGRY = 'CAACAgIAAyEGAATJg9QWAAI9S2oQn5yUP74zmVr30B19LfNJQ5BOAAI7mAACnMCJSJCUxis28mu_OwQ'
STICKER_LAUGH = 'CAACAgIAAyEFAATg5w4fAAPVahCKEgqm6gMnTmhlbkJ7WPLWFrEAAianAAI6pIBIsOEtVY3_4tA7BA'
STICKER_THINK = 'CAACAgIAAyEFAATg5w4fAAIBEmoQjoFARfSHEhf5BhIvBpK1C3P0AALFqAACdOR4SBlpuri97s0XOwQ'
STICKER_DRAMA = 'CAACAgIAAyEFAATg5w4fAAPaahCKJAwwbq0ed6ibgQKXp0aw1yYAArmaAAKQpIBIYKoHrwPakx87BA'

# Списки ответов
jokes = ["🎭 ЗНАЕШЬ КАКОЕ САМОЕ ЛОХОНУТОЕ СОЗДАНИЕ? ВЕРНО, ТЫ!", "🎭 Представь если бы ты был в моей иллюзии... ХАХАХА"]
insult_replies = ["🎭 НУ И НУ! ПОВЕРЬ, ОНИ ТЕБЕ НИЧЕМ НЕ ПОМОГУТ.", "🎭 Ублюдок? Какое низкое слово."]
magic_answers = ["Да.", "Нет.", "Возможно."]

# Команды
@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("🎭 Шамиль (Шадоу Милк) НА СЦЕНЕ. ГОТОВЫ ЛИ ВЫ К ДРАМЕ?")
    await message.answer_sticker(STICKER_DRAMA)

@dp.message(Command("joke"))
async def joke(message: Message):
    await message.answer(random.choice(jokes))
    await message.answer_sticker(STICKER_LAUGH)

# Реакция на вопросы
@dp.message(F.text.lower().contains("шамиль") & F.text.contains("?"))
async def handle_shamil_question(message: Message):
    await message.answer(random.choice(magic_answers))
    await message.answer_sticker(STICKER_THINK)

# Реакция на мат
@dp.message(F.text.lower().contains(tuple(['сука', 'бля', 'пидор', 'дебил', 'блят', 'блять', 'пошёл', 'ублюдок'])))
async def handle_bad_words(message: Message):
    await message.answer(random.choice(insult_replies))
    await message.answer_sticker(STICKER_ANGRY)

# Запуск
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
