import asyncio
import random
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = '8684676356:AAFn3L9uhbGqHymJzanCFmTvDnBVWZKklLQ'

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Твои списки
jokes = [
    "🎭 ЗНАЕШЬ КАКОЕ САМОЕ ЛОХОНУТОЕ СОЗДАНИЕ? ВЕРНО, ТЫ!",
    "🎭 Представь если бы ты был в моей иллюзии, то как бы я с тобой относился? ПРАВИЛЬНО, КАК К МАРИОНЕТКЕ! ХАХАХА",
    "🎭 ЗНАЕШЬ ПОЧЕМУ ПРОГРАММИСТЫ НЕ ЛЮБЯТ ПРИРОДУ? ПОТОМУ ЧТО ТАМ НЕ ИНТЕРЕСНО, БЫТЬ ОДНИМ ЛЕГЧЕ СИДЕТЬ ДОМА И ИГРАТЬ СО СВОИМ СОЗДАННЫМ!",
    "🎭 Если так подумать, то у меня нет мамы, но есть создательница, которая разрешает делать всё, что я только захочу. ТАК ЧТО ЗАВИДУЙ!",
    "🎭 Поверь, я не просто какой-то бот, я действительно могу всё запоминать — каждое слово, которым ты меня оскорбляешь."
]

bad_words = ['сука', 'бля', 'пидор', 'дебил', 'блят', 'блять', 'пошёл', 'ублюдок']
insult_replies = [
    "🎭 НУ И НУ! ПОВЕРЬ, ОНИ ТЕБЕ НИЧЕМ НЕ ПОМОГУТ. ПОМОЧЬ СЕБЕ МОЖЕШЬ ТОЛЬКО ТЫ.",
    "🎭 Ай-яй-яй, тебя уже учили, что нельзя материться! А ты! НУ ХОТЯ МНЕ РАЗРЕШАЮТ ВСЁ, ПОКА ТЕБЯ НЕТ.",
    "🎭 Ну и ну, как не стыдно! ДАЖЕ Я ТАК НЕ ДЕЛАЮ. Ведь это противно.",
    "🎭 Ублюдок? Какое низкое слово для столь ничтожного существа, как ты."
]

magic_answers = ["Да.", "Нет.", "Маловероятно.", "Возможно.", "Ха! Ты серьезно ждешь от меня правды?"]

# --- ОБРАБОТЧИКИ ---

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("🎭 Шамиль (Шадоу Милк) НА СЦЕНЕ. ГОТОВЫ ЛИ ВЫ К ДРАМЕ?")

@dp.message(Command("joke"))
async def joke(message: Message):
    await message.answer(random.choice(jokes))

# Реакция на мат (стоит ПЕРЕД остальными текстовыми сообщениями)
@dp.message(F.text.lower().contains(tuple(bad_words)))
async def handle_bad_words(message: Message):
    await message.answer(random.choice(insult_replies))

# Реакция на вопрос с именем
@dp.message(F.text.lower().contains("шамиль") & F.text.contains("?"))
async def handle_shamil_question(message: Message):
    await message.answer(random.choice(magic_answers))

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
