import asyncio
import random
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

TOKEN = '8684676356:AAFn3L9uhbGqHymJzanCFmTvDnBVWZKklLQ'

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ========== ОЧКИ ==========
user_scores = {}

# ========== СТИКЕРЫ ==========
STICKER_ANGRY = 'CAACAgIAAyEGAATJg9QWAAI9S2oQn5yUP74zmVr30B19LfNJQ5BOAAI7mAACnMCJSJCUxis28mu_OwQ'
STICKER_LAUGH = 'CAACAgIAAyEFAATg5w4fAAPVahCKEgqm6gMnTmhlbkJ7WPLWFrEAAianAAI6pIBIsOEtVY3_4tA7BA'
STICKER_THINK = 'CAACAgIAAyEFAATg5w4fAAIBEmoQjoFARfSHEhf5BhIvBpK1C3P0AALFqAACdOR4SBlpuri97s0XOwQ'
STICKER_DRAMA = 'CAACAgIAAyEFAATg5w4fAAPaahCKJAwwbq0ed6ibgQKXp0aw1yYAArmaAAKQpIBIYKoHrwPakx87BA'

# ========== КНОПКИ ==========
button_chaos = KeyboardButton(text="🔥 Устроить хаос!")
button_show = KeyboardButton(text="🎭 Показать шоу!")
button_boredom = KeyboardButton(text="💡 Изгнать скуку!")
button_kingdom = KeyboardButton(text="🏰 В Королевство!")

keyboard = ReplyKeyboardMarkup(
    keyboard=[[button_chaos, button_show], [button_boredom, button_kingdom]],
    resize_keyboard=True
)

# ========== БАЗА РЕАКЦИЙ ==========
chaos_responses = [
    "🎭 *ХА-ОС!* Ты выпустил джинна из тряпки! Получай видео: [случайное видео]",
    "🎭 Шамиль щёлкает пальцами — и в чате появляется Теневой Виноград! 🍇 Он украл 5 очков у @user",
    "🎭 Ваниль споткнулся о ведро и уронил занавес! Сцена хаотично меняется!",
    "🎭 Хаос-лотерея: @user должен рассказать анекдот про клоуна!",
    "🎭 Шамиль чихнул — и текст в чате перевернулся вверх ногами!"
]

show_responses = [
    "🎭 *Шоу начинается!* Смотрю на вас... и превращаю @user в тряпку! Ха-ха!",
    "🎭 *Колесо эмоций!* Выпало: ЗЛОСТЬ. Сейчас я буду кричать на @user. +5 очков за смелость!",
    "🎭 *Суд над Ванилем!* Ваниль обвиняется в том, что слишком мокрый. Адвокат: @user. Что скажешь?",
    "🎭 *Магический ритуал!* Чтобы призвать хаос, крикните «Кукареку»!",
    "🎭 *Сломанный робот!* Бип-буп... Я даю сбой... ШУТКА! Хаос перезагружен."
]

boredom_responses = [
    "💡 *Задание:* нарисуй Шамиля в стиле «пиксель-арт» и отправь в чат!",
    "💡 *Викторина:* сколько у Шамиля масок? (Ответ: бесконечность)",
    "💡 *Конкурс:* придумай новое имя для Ваниля. Лучшее получит +10 очков!",
    "💡 *Загадка:* что делает Шамиль, когда никто не видит? (Принимается любой абсурд!)",
    "💡 *Битва мемов:* отправь мем про театр. Шамиль выберет лучший!"
]

kingdom_responses = [
    "🏰 *Добро пожаловать!* Твои игры: /game1 — вопросы, /game2 — удача, /game3 — пытка",
    "🏰 *Королевство в опасности!* Теневой Виноград украл корону. Напиши /detective",
    "🏰 *Турнир марионеток:* у тебя 3 жизни. Напиши /fight, чтобы сразиться с ботом",
    "🏰 *Лабиринт иллюзий:* выбери дверь: А) Красную Б) Синюю",
    "🏰 *Театральный батл:* @user против @user2. Кто больше рассмешит чат?"
]

jokes = [
    "🎭 Твой интеллект — это демо-версия, срок действия которой истек.",
    "🎭 Шамиль всё видит. Шамиль всё помнит. И Шамиль знает, что ты ЛОХАНДЕР.",
    "🎭 Знаешь, почему программисты ненавидят реальность? Потому что в коде всё логично, а ты — это хаос."
]

# ========== КОМАНДЫ ==========
@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🎭 *Шамиль НА СЦЕНЕ!*\n\nЖми на кнопки, марионетка! Хаос ждёт!",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

@dp.message(F.text == "🔥 Устроить хаос!")
async def chaos_button(message: Message):
    response = random.choice(chaos_responses)
    response = response.replace("@user", message.from_user.first_name)
    await message.answer(response, parse_mode="Markdown")
    await message.answer_sticker(STICKER_LAUGH)

@dp.message(F.text == "🎭 Показать шоу!")
async def show_button(message: Message):
    response = random.choice(show_responses)
    response = response.replace("@user", message.from_user.first_name)
    await message.answer(response, parse_mode="Markdown")
    await message.answer_sticker(STICKER_DRAMA)

@dp.message(F.text == "💡 Изгнать скуку!")
async def boredom_button(message: Message):
    response = random.choice(boredom_responses)
    await message.answer(response, parse_mode="Markdown")
    await message.answer_sticker(STICKER_THINK)

@dp.message(F.text == "🏰 В Королевство!")
async def kingdom_button(message: Message):
    response = random.choice(kingdom_responses)
    response = response.replace("@user", message.from_user.first_name)
    await message.answer(response, parse_mode="Markdown")
    await message.answer_sticker(STICKER_DRAMA)

@dp.message(Command("spin"))
async def spin_wheel(message: Message):
    user_id = message.from_user.id
    if user_id not in user_scores:
        user_scores[user_id] = 0

    sector = random.choice(['ХАОС!', 'ПРИЗ', 'ПРОКЛЯТИЕ', 'ТЕАТР', 'ДЖЕКПОТ'])

    if sector == 'ХАОС!':
        await message.answer(f"🎭 *ВЫПАЛО:* {sector}\n\n{random.choice(jokes)}", parse_mode="Markdown")
    elif sector == 'ПРИЗ':
        user_scores[user_id] += 10
        await message.answer(f"🎭 *ВЫПАЛО:* {sector}\n\n✨ +10 очков! Счёт: {user_scores[user_id]}", parse_mode="Markdown")
    elif sector == 'ПРОКЛЯТИЕ':
        user_scores[user_id] -= 5
        await message.answer(f"🎭 *ВЫПАЛО:* {sector}\n\n💀 -5 очков! Счёт: {user_scores[user_id]}", parse_mode="Markdown")
    elif sector == 'ТЕАТР':
        await message.answer(f"🎭 *ВЫПАЛО:* {sector}\n\n🎭 Расскажи Шамилю, почему ты всё ещё здесь?", parse_mode="Markdown")
    elif sector == 'ДЖЕКПОТ':
        user_scores[user_id] += 50
        await message.answer_sticker(STICKER_LAUGH)
        await message.answer(f"🎭 *ДЖЕКПОТ!*\n\n🌟 +50 очков! Счёт: {user_scores[user_id]}", parse_mode="Markdown")

    await message.answer_sticker(STICKER_THINK)

@dp.message(Command("top"))
async def show_top(message: Message):
    if not user_scores:
        await message.answer("🎭 Никто ещё не крутил колесо! /spin", parse_mode="Markdown")
        return
    sorted_scores = sorted(user_scores.items(), key=lambda x: x[1], reverse=True)
    top_text = "🏆 *ТОП МАРИОНЕТОК* 🏆\n\n"
    for idx, (user_id, score) in enumerate(sorted_scores[:5], 1):
        user = await bot.get_chat(user_id)
        top_text += f"{idx}. {user.first_name} — {score} очков\n"
    await message.answer(top_text, parse_mode="Markdown")

# ========== ФИЛЬТРАЦИЯ МАТА ==========
BAD_WORDS = {'сука', 'бля', 'пидор', 'дебил', 'блят', 'блять', 'пошёл', 'ублюдок'}

@dp.message()
async def filter_bad_words(message: Message):
    if any(word in message.text.lower() for word in BAD_WORDS):
        await message.answer("🎭 Ай-яй-яй, я не буду это слушать!")
        await message.answer_sticker(STICKER_ANGRY)

# ========== ЗАПУСК ==========
async def main():
    print("🎭 Шамиль запущен. Театр открыт!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
