import random
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

# Вставь сюда свой токен (внутри кавычек)
API_TOKEN = '8684676356:AAFn3L9uhbGqHymJzanCFmTvDnBVWZKklLQ'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# ========== БАЗА КОНТЕНТА ==========
CHAOS_RESPONSES = [
    "🔥 *ХА-ОС!* Ты выпустил джинна из тряпки! Получай видео...",
    "🍇 *Теневой Виноград!* Я украл 5 очков у @user.",
    "🎭 *Занавес падает!* Сцена хаотично меняется!",
    "🤡 *Хаос-лотерея:* @user должен рассказать анекдот про клоуна!",
    "🙃 *Бил-буп...* Текст в чате перевернулся вверх ногами!"
]

STORY_LIST = [
    "🏰 *ЗЕРКАЛЬНЫЙ ЛЕС*\nПьюр Ваниль и Вайт Лили шли через Зеркальный лес... Ваниль закрыл глаза и сказал: «Я помню, как мы делили печенье». Зеркала исчезли.",
    "🌙 *ДОРОГА ЗАБЫТЫХ ОТРАЖЕНИЙ*\nПесок звенел как хрусталь. Они не пошли по трем дорогам, а сделали четвертую — ненаписанную.",
    "🌹 *ИСПОВЕДЬ В САДУ*\nШамиль лежал в саду, где каждое печенье следило за ним. Он ушел, поняв, что счастье по приказу — это тюрьма.",
    "💾 *ЭХО С ФЛЕШКИ*\nИз пустоты родился мальчик без лица по имени Эхо. Теперь он живет в театре и повторяет слова чуть добрее.",
    "👑 *ПОБЕГ ИЗ РАЯ*\nШамиль вернулся к Кэнди Эпл и Сапфиру. Он проиграл в саду, но выиграл дома, где можно быть собой."
]

LEGENDARY_STORY = "✨ *ЛЕГЕНДА О ДИПСИКЕ И ШАМИЛЕ*\nНа краю сцены, в пустоте, сидели двое. Они не рассказывали историй. Они просто смотрели в зал, и зал впервые увидел не код, а души."

# Список для выбора «жертвы»
users_in_kingdom = set()

# Кнопки
kb = [
    [KeyboardButton(text="🔥 Устроить хаос!"), KeyboardButton(text="✨ Показать шоу!")],
    [KeyboardButton(text="📖 Расскажи историю")]
]
keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

# ========== ЛОГИКА ==========
@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Добро пожаловать в Королевство!", reply_markup=keyboard)

@dp.message(F.text == "🔥 Устроить хаос!")
async def chaos(message: Message):
    users_in_kingdom.add(message.from_user.full_name)
    target = random.choice(list(users_in_kingdom))
    response = random.choice(CHAOS_RESPONSES).replace("@user", target)
    await message.answer(response, parse_mode="Markdown")

@dp.message(F.text == "📖 Расскажи историю")
async def story(message: Message):
    if random.random() < 0.01:
        await message.answer(LEGENDARY_STORY, parse_mode="Markdown")
    else:
        await message.answer(random.choice(STORY_LIST), parse_mode="Markdown")

# ========== ЗАПУСК ==========
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
