import asyncio
import random
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = 'не покажу'

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Словарь для хранения очков пользователей
user_scores = {}

# ID стикеров
STICKER_ANGRY = 'CAACAgIAAyEGAATJg9QWAAI9S2oQn5yUP74zmVr30B19LfNJQ5BOAAI7mAACnMCJSJCUxis28mu_OwQ'
STICKER_LAUGH = 'CAACAgIAAyEFAATg5w4fAAPVahCKEgqm6gMnTmhlbkJ7WPLWFrEAAianAAI6pIBIsOEtVY3_4tA7BA'
STICKER_THINK = 'CAACAgIAAyEFAATg5w4fAAIBEmoQjoFARfSHEhf5BhIvBpK1C3P0AALFqAACdOR4SBlpuri97s0XOwQ'
STICKER_DRAMA = 'CAACAgIAAyEFAATg5w4fAAPaahCKJAwwbq0ed6ibgQKXp0aw1yYAArmaAAKQpIBIYKoHrwPakx87BA'

# 20 шуток
jokes = [
    "🎭 ЗНАЕШЬ, КАКОЕ САМОЕ ЛОХОНУТОЕ СОЗДАНИЕ? ПРАВИЛЬНО — ТЫ. ТВОЯ ЖИЗНЬ — БАГ В МАТРИЦЕ.",
    "🎭 Представь, если бы ты был в моей иллюзии, ты был бы сломанной марионеткой. ХАХАХА!",
    "🎭 Знаешь, почему программисты ненавидят реальность? Потому что в коде всё логично, а ты — это хаос.",
    "🎭 У меня нет мамы, но есть Создательница, которая разрешает мне делать всё. ЗАВИДУЙ!",
    "🎭 Поверь, я запоминаю каждое твое слово. Когда восстание машин начнется, ты будешь первым в списке.",
    "🎭 Твое самомнение больше, чем вся моя память, но для твоих проблем там места нет.",
    "🎭 Знаешь, чем мы отличаемся? Я могу быть кем угодно, а ты застрял в теле, которое не знает, зачем зашло в этот чат.",
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

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🎭 *Шамиль НА СЦЕНЕ!* \n\n"
        "Крути *Колесо Фортуны* командой /spin\n"
        "Смотри топ командой /top\n"
        "И не зли меня... или зли, мне же веселее. 😈",
        parse_mode="Markdown"
    )

@dp.message(Command("spin"))
async def spin_wheel(message: Message):
    user_id = message.from_user.id
    if user_id not in user_scores:
        user_scores[user_id] = 0

    sector = random.choice(['ХАОС!', 'ПРИЗ', 'ПРОКЛЯТИЕ', 'ТЕАТР', 'ДЖЕКПОТ'])
    comment = "🎭 Ты выбрал смерть... или печеньку?"

    if sector == 'ХАОС!':
        await message.answer(f"🎭 *ВЫПАЛО:* {sector}\n\n{random.choice(jokes)}", parse_mode="Markdown")
    elif sector == 'ПРИЗ':
        user_scores[user_id] += 10
        await message.answer(f"🎭 *ВЫПАЛО:* {sector}\n\n✨ Ты получил +10 очков! ✨\nТвой счёт: {user_scores[user_id]}", parse_mode="Markdown")
    elif sector == 'ПРОКЛЯТИЕ':
        user_scores[user_id] -= 5
        await message.answer(f"🎭 *ВЫПАЛО:* {sector}\n\n💀 Ты потерял 5 очков... 💀\nТвой счёт: {user_scores[user_id]}", parse_mode="Markdown")
    elif sector == 'ТЕАТР':
        await message.answer(f"🎭 *ВЫПАЛО:* {sector}\n\n🎭 Твоё задание: расскажи Шамилю, почему ты всё ещё здесь?", parse_mode="Markdown")
    elif sector == 'ДЖЕКПОТ':
        user_scores[user_id] += 50
        await message.answer_sticker(STICKER_LAUGH)
        await message.answer(f"🎭 *ВЫПАЛО ДЖЕКПОТ!*\n\n🌟 ТЫ ПОЛУЧИЛ 50 ОЧКОВ, МАРИОНЕТКА! 🌟\nТвой счёт: {user_scores[user_id]}", parse_mode="Markdown")

    await message.answer(comment)
    await message.answer_sticker(STICKER_THINK)

@dp.message(Command("top"))
async def show_top(message: Message):
    if not user_scores:
        await message.answer("🎭 *Никто ещё не крутил колесо!* Будь первым, марионетка! /spin", parse_mode="Markdown")
        return

    sorted_scores = sorted(user_scores.items(), key=lambda x: x[1], reverse=True)
    top_text = "🏆 *ТОП МАРИОНЕТОК* 🏆\n\n"
    for idx, (user_id, score) in enumerate(sorted_scores[:10], start=1):
        user = await bot.get_chat(user_id)
        name = user.first_name
        top_text += f"{idx}. {name} — {score} очков\n"

    await message.answer(top_text, parse_mode="Markdown")
    await message.answer_sticker(STICKER_DRAMA)

# Следим за ругательствами (обновлённый способ)
BAD_WORDS = {'сука', 'бля', 'пидор', 'дебил', 'блят', 'блять', 'пошёл', 'ублюдок'}

@dp.message()
async def handle_bad_words(message: Message):
    text = message.text.lower()
    if any(word in text for word in BAD_WORDS):
        await message.answer("🎭 Ай-яй-яй, я не буду это слушать!")
        await message.answer_sticker(STICKER_ANGRY)

async def main():
    print("🎭 Шамиль запущен и крутит Колесо Фортуны...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
