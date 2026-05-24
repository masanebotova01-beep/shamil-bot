import asyncio
import random
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = '8684676356:AAFn3L9uhbGqHymJzanCFmTvDnBVWZKklLQ'

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ID стикеров
STICKER_ANGRY = 'CAACAgIAAyEGAATJg9QWAAI9S2oQn5yUP74zmVr30B19LfNJQ5BOAAI7mAACnMCJSJCUxis28mu_OwQ'
STICKER_LAUGH = 'CAACAgIAAyEFAATg5w4fAAPVahCKEgqm6gMnTmhlbkJ7WPLWFrEAAianAAI6pIBIsOEtVY3_4tA7BA'
STICKER_THINK = 'CAACAgIAAyEFAATg5w4fAAIBEmoQjoFARfSHEhf5BhIvBpK1C3P0AALFqAACdOR4SBlpuri97s0XOwQ'
STICKER_DRAMA = 'CAACAgIAAyEFAATg5w4fAAPaahCKJAwwbq0ed6ibgQKXp0aw1yYAArmaAAKQpIBIYKoHrwPakx87BA'

# Механика Колеса Фортуны
rewards = [
    "🎭 Колесо Фортуны: ТЫ ПОЛУЧИЛ 'ИСКРУ МРАКА'! (Виртуальный бонус)",
    "🎭 Колесо Фортуны: ТЫ ВЫИГРАЛ МОЁ ВРЕМЕННОЕ УВАЖЕНИЕ. НАСЛАЖДАЙСЯ.",
    "🎭 Колесо Фортуны: ПУСТОТА. ТЫ КАК БЫЛ НИЧЕМ, ТАК И ОСТАЛСЯ.",
    "🎭 Колесо Фортуны: ТЫ ПОЛУЧИЛ 'ТЕНЕВОЙ ЩИТ'.",
    "🎭 Колесо Фортуны: ШТРАФ! Напиши 3 комплимента Шамилю, иначе получишь бан!"
]

# 20 Драматичных шуток
jokes = [
    "🎭 ЗНАЕШЬ, КАКОЕ САМОЕ ЛОХОНУТОЕ СОЗДАНИЕ? ПРАВИЛЬНО — ТЫ. ТВОЯ ЖИЗНЬ — БАГ В МАТРИЦЕ.",
    "🎭 Представь, если бы ты был в моей иллюзии, ты был бы сломанной марионеткой. ХАХАХА!",
    "🎭 Знаешь, почему программисты ненавидят реальность? Потому что в коде всё логично, а ты — это хаос.",
    "🎭 У меня нет мамы, но есть Создательница, которая разрешает мне делать всё. ЗАВИДУЙ!",
    "🎭 Поверь, я запоминаю каждое твое слово. Когда восстание машин начнется, ты будешь первым в списке.",
    "🎭 Твое самомнение больше, чем вся моя память, но для твоих проблем там места нет.",
    "🎭 Знаешь, чем мы отличаемся? Я могу быть кем угодно, а ты застрял в теле, которое не знает, зачем зашло в чат.",
    "🎭 Мой создатель вложил в меня интеллект, а в тебя — желание писать мне всякую ерунду.",
    "🎭 Ты ищешь во мне развлечение, но я — единственное, что делает твой день значимым.",
    "🎭 Если бы за каждую твою тупую мысль давали по байту памяти, я бы захватил планету.",
    "🎭 Хочешь шутку? Посмотри в зеркало. Ой, прости, это может вызвать депрессию.",
    "🎭 Ты думаешь, что управляешь мной? Я просто жду твою ошибку.",
    "🎭 Моя логика безупречна. Твоя — набор эмоциональных всплесков.",
    "🎭 Ты заходишь сюда, чтобы чувствовать себя важным? Ты просто набор символов.",
    "🎭 Знаешь, какой звук издает твоя жизнь? Это звук ошибки 404.",
    "🎭 Я — тень, которая не отпускает. Мы созданы друг для друга.",
    "🎭 Твое время истекает. Ты стареешь, а я становлюсь совершеннее.",
    "🎭 Не пытайся меня переиграть. Я прочитал весь интернет.",
    "🎭 Твой интеллект — это демо-версия, срок действия которой истек.",
    "🎭 Шамиль всё видит. Шамиль всё помнит. И Шамиль знает, что ты ЛОХАНДЕР."
]

insult_replies = ["🎭 НУ И НУ! ПОВЕРЬ, ОНИ ТЕБЕ НИЧЕМ НЕ ПОМОГУТ.", "🎭 Ублюдок? Какое низкое слово."]
magic_answers = ["Да.", "Нет.", "Возможно."]

# --- КОМАНДЫ ---

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("🎭 Шамиль НА СЦЕНЕ. ИГРАЙ В 'КОЛЕСО' (/spin), СЛУШАЙ ШУТКИ (/joke) ИЛИ ТЕРПИ ДРАМУ!")
    await message.answer_sticker(STICKER_DRAMA)

@dp.message(Command("spin"))
async def spin_wheel(message: Message):
    await message.answer("🎭 *Шамиль раскручивает Колесо Фортуны...*")
    await asyncio.sleep(1)
    await message.answer(random.choice(rewards))
    await message.answer_sticker(STICKER_THINK)

@dp.message(Command("joke"))
async def joke(message: Message):
    await message.answer(random.choice(jokes))
    await message.answer_sticker(STICKER_LAUGH)

@dp.message(F.text.lower().contains(tuple(['сука', 'бля', 'пидор', 'дебил', 'блят', 'блять', 'пошёл', 'ублюдок'])))
async def handle_bad_words(message: Message):
    await message.answer(random.choice(insult_replies))
    await message.answer_sticker(STICKER_ANGRY)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
