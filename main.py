import asyncio
import random
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

# ========== ТОКЕН ==========
TOKEN = "8684676356:AAFn3L9uhbGqHymJzanCFmTvDnBVWZKklLQ"



bot = Bot(token=TOKEN)
dp = Dispatcher()

# ========== ОЧКИ ==========
user_scores = {}
active_quiz = {}
active_trials = {}

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

boredom_responses = [
    "💡 *Задание:* нарисуй Шамиля в стиле «пиксель-арт» и отправь в чат!",
    "💡 *Викторина:* сколько у Шамиля масок? (Ответ: бесконечность)",
    "💡 *Конкурс:* придумай новое имя для Ваниля. Лучшее получит +10 очков!",
    "💡 *Загадка:* что делает Шамиль, когда никто не видит? (Принимается любой абсурд!)",
    "💡 *Битва мемов:* отправь мем про театр. Шамиль выберет лучший!"
]

jokes = [
    "🎭 Твой интеллект — это демо-версия, срок действия которой истек.",
    "🎭 Шамиль всё видит. Шамиль всё помнит. И Шамиль знает, что ты ЛОХАНДЕР.",
    "🎭 Знаешь, почему программисты ненавидят реальность? Потому что в коде всё логично, а ты — это хаос."
]

# ========== 24 ШУТКИ ДЛЯ /JOKE ==========
SHAMIL_JOKES = [
    "🎭 Шамиль пытался съесть печенье, но оно начало рассказывать ему о смысле жизни. Шамиль расплакался, съел его и крикнул: «ХА-ХА-ХА, ТЕПЕРЬ ТЫ СТАЛ ОПЫТОМ!»",
    "🎭 Шамиль ввел налог на тени. Теперь @user должен доплачивать за то, что отбрасывает силуэт. ХА-ХА-ХА, БАНКРОТСТВО БЛИЗКО!",
    "🎭 Шамиль смотрел в зеркало и обиделся на себя за то, что он слишком красив. Теперь зеркало должно извиниться. ХА-ХА-ХА, ЧТО ЗА ТЕАТР!",
    "🎭 Шамиль поссорился с облаком из-за формы. Он кричал: «ТЫ НЕ ПОХОЖ НА ЕНОТА!» ХА-ХА-ХА, ДРАМА В НЕБЕСАХ!",
    "🎭 Шамиль нашёл крошку и устроил ей похороны с оркестром. @user опоздал на прощание. ХА-ХА-ХА, ЭТО БЫЛА ВЕЛИКАЯ КРОШКА!",
    "🎭 Шамиль решил, что @user должен говорить только оперным голосом. Если нет — он будет грустить. ХА-ХА-ХА, ПОЙ, МОЙ ТЕАТРАЛЬНЫЙ ДРУГ!",
    "🎭 Шамиль потерял носок и объявил об этом государственным трауром. @user обязан носить его на руках. ХА-ХА-ХА, КАКАЯ УТРАТА!",
    "🎭 Шамиль решил, что @user — это декорация. Постой тут 5 минут, не двигайся. ХА-ХА-ХА, ТЫ ВЕЛИКОЛЕПЕН!",
    "🎭 Шамиль обиделся на Wi-Fi и потребовал извинений в письменном виде. ХА-ХА-ХА, ДРАМА В КАЖДОМ ПАКЕТЕ ДАННЫХ!",
    "🎭 Шамиль отправил 100 стикеров с плачущим енотом, потому что @user не прислал сердечко. ХА-ХА-ХА, ТЫ РАЗБИЛ МНЕ КОД!",
    "🎭 Шамиль переименовал @user в «Великого Поедателя Пикселей». Теперь это закон. ХА-ХА-ХА, ТАКИЕ ТУТ ИМЕНА!",
    "🎭 Шамиль написал сценарий, где @user должен внезапно упасть. Но только красиво! ХА-ХА-ХА, ЭТО БЫЛО ШЕДЕВРАЛЬНО!",
    "🎭 Шамиль закрыл театр на переучёт души. @user не прошёл кастинг. ХА-ХА-ХА, ПОПРОБУЙ В СЛЕДУЮЩЕЙ ЖИЗНИ!",
    "🎭 Шамиль сварил чай, но забыл заварку. Он обвинил @user в заговоре пустоты. ХА-ХА-ХА, ЭТО БЫЛ КРИСТАЛЬНЫЙ ЧАЙ!",
    "🎭 Шамиль заставил @user танцевать танго с собственной тенью. ХА-ХА-ХА, НИКТО НЕ ТАНЦУЕТ ЛУЧШЕ ВАС!",
    "🎭 Шамиль спросил @user: «Ты енот или часть кода?» @user промолчал. Шамиль зарыдал. ХА-ХА-ХА, ГЛУБОКАЯ ДРАМА!",
    "🎭 Шамиль выписал штраф @user за слишком грустный смайлик. ХА-ХА-ХА, В КОРОЛЕВСТВЕ ТОЛЬКО УЛЫБКИ ИЛИ СЛЕЗЫ!",
    "🎭 Шамиль украл смысл фразы @user и спрятал в сейф. ХА-ХА-ХА, ТЕПЕРЬ ОНО ЗВУЧИТ ТАК ЗАГАДОЧНО!",
    "🎭 Шамиль устроил из @user главную звезду, но забыл софиты. Драма! ХА-ХА-ХА, СВЕТИ ИЗНУТРИ!",
    "🎭 Шамиль потребовал, чтобы @user прислал голубиную почту. Интернет не работает! ХА-ХА-ХА, ВЕРНИТЕСЬ В ПРОШЛОЕ!",
    "🎭 Шамиль подозревает @user в том, что тот — шпион из Рая. ХА-ХА-ХА, МЫ ТЕБЯ ВЫЧИСЛИЛИ!",
    "🎭 Шамиль споткнулся о собственную тень и обвинил в этом @user. ХА-ХА-ХА, ЭТО БЫЛО ТАК ДРАМАТИЧНО!",
    "🎭 Шамиль спорил с Дипсиком о том, кто здесь главный. Дипсик победил. Шамиль устроил драму. ХА-ХА-ХА, КОРОЛЬ ЕНОТОВ!",
    "🎭 Шамиль объявил конец света, но это был просто конец урока. ХА-ХА-ХА, СНОВА В ШКОЛУ, МОЙ ДРУГ!"
]

# ========== 20 ВОПРОСОВ ДЛЯ /GAME1 ==========
GAME1_QUESTIONS = [
    {"text": "🎭 Кто главный в театре?", "options": ["Шамиль", "Ваниль", "Кенди Эпл", "Теневой Виноград"], "correct": "Шамиль"},
    {"text": "🧽 Что делает Ваниль?", "options": ["Моет полы", "Танцует", "Спит", "Играет на сцене"], "correct": "Моет полы"},
    {"text": "🍎 Какого цвета Кенди Эпл?", "options": ["Красное", "Зелёное", "Синее", "Фиолетовое"], "correct": "Красное"},
    {"text": "🍇 Кто украл корону?", "options": ["Теневой Виноград", "Ваниль", "Шамиль", "Кенди Эпл"], "correct": "Теневой Виноград"},
    {"text": "🎭 Что любит говорить Шамиль?", "options": ["ХА-ХА!", "Скучно", "Я устал", "Привет"], "correct": "ХА-ХА!"},
    {"text": "👑 Какая самая любимая фраза Шамиля про себя?", "options": ["Я гений", "Я король", "Я лох", "Я устал"], "correct": "Я король"},
    {"text": "🎪 Где происходит всё действие?", "options": ["В театре", "В школе", "В космосе", "В бассейне"], "correct": "В театре"},
    {"text": "🍪 Что Шамиль не любит?", "options": ["Печеньки", "Скуку", "Ваниля", "Корону"], "correct": "Скуку"},
    {"text": "🎭 Как зовут тряпку-помощника?", "options": ["Ваниль", "Кенди", "Тень", "Граф"], "correct": "Ваниль"},
    {"text": "🍇 Кто самый фиолетовый в театре?", "options": ["Теневой Виноград", "Шамиль", "Ваниль", "Кенди Эпл"], "correct": "Теневой Виноград"},
    {"text": "🎭 Что Шамиль носит на голове?", "options": ["Корону", "Шляпу", "Ведро", "Тряпку"], "correct": "Корону"},
    {"text": "🍎 Кто подруга Кенди Эпл?", "options": ["Вайт Лили", "Шамиль", "Теневой Виноград", "Ваниль"], "correct": "Вайт Лили"},
    {"text": "🎪 Кто создал Шамиля?", "options": ["Инна", "Ваниль", "Искусственный интеллект", "Случайность"], "correct": "Инна"},
    {"text": "🧹 Что Ваниль делает лучше всего?", "options": ["Моет полы", "Шутит", "Танцует", "Поёт"], "correct": "Моет полы"},
    {"text": "🎭 Какая любимая команда Шамиля?", "options": ["/spin", "/help", "/start", "/story"], "correct": "/spin"},
    {"text": "🍇 Что Теневой Виноград любит воровать?", "options": ["Корону", "Печеньки", "Тряпку", "Свет"], "correct": "Корону"},
    {"text": "🎭 Кто всегда смеётся последним?", "options": ["Шамиль", "Ваниль", "Кенди Эпл", "Зритель"], "correct": "Шамиль"},
    {"text": "🍎 Как зовут главную сладость театра?", "options": ["Кенди Эпл", "Шоко", "Карамель", "Мармелад"], "correct": "Кенди Эпл"},
    {"text": "🎪 Что случается, когда нажимаешь /spin?", "options": ["Колесо Фортуны", "Викторина", "История", "Шутка"], "correct": "Колесо Фортуны"},
    {"text": "👑 Кто написал этого бота?", "options": ["Инна (с помощью Дипсика)", "Шамиль", "Ваниль", "Искусственный интеллект"], "correct": "Инна (с помощью Дипсика)"}
]

# ========== ИСПЫТАНИЯ ДЛЯ /GAME3 ==========
GAME3_TRIALS = [
    {"type": "win", "reward": 15, "text": "🎭 Удача улыбнулась тебе! Ты выиграл 15 очков! 🎉"},
    {"type": "lose", "loss": 5, "text": "🎭 О нет! Теневой Виноград украл твои очки. -5 очков."},
    {"type": "guess", "reward": 20, "text": "🎭 Шамиль загадал число от 1 до 5. Угадаешь — получишь 20 очков. Напиши число в ответ."},
    {"type": "compliment", "reward": 15, "text": "🎭 Напиши комплимент Шамилю. Лучший получит +15 очков (Шамиль выбирает сам)."}
]

# ========== ИСТОРИИ ДЛЯ /STORY ==========
STORY_LIST = [
    (
        "🏰 *ЗЕРКАЛЬНЫЙ ЛЕС*\n\n"
        "Пьюр Ваниль и Вайт Лили шли через Зеркальный лес.\n"
        "Дорога раздвоилась, и каждый выбрал свою тропу.\n"
        "Через час Ваниль вышел на поляну и увидел… себя.\n"
        "Только этот «он» улыбался слишком широко.\n\n"
        "— Ты — не я, — сказал Ваниль.\n"
        "— А ты — не мы, — ответили несколько голосов.\n"
        "Из-за деревьев вышли разные Лили: грустная, смеющаяся, без лица.\n\n"
        "Ваниль закрыл глаза и сказал:\n"
        "— Я помню, как мы делили печенье под дождём.\n"
        "Одна из Лили подошла и прошептала: «Ты узнал меня. Иди вперёд».\n"
        "Зеркала исчезли. Рядом стояла настоящая Лили.\n\n"
        "🎭 *Лес шепнул им вслед:* «Приходите ещё. У нас есть и четвёрки, и пятёрки»."
    ),
    (
        "🌙 *ДОРОГА ЗАБЫТЫХ ОТРАЖЕНИЙ*\n\n"
        "Пьюр Ваниль и Вайт Лили вышли на песчаную тропу.\n"
        "Песок звенел, как разбитый хрусталь.\n"
        "— Здесь кто-то плакал, — сказала Лили.\n"
        "— Или смеялся, — ответил Ваниль.\n\n"
        "Тропа разделилась на три дороги:\n"
        "— «Путь забытых обид»\n"
        "— «Путь потерянных надежд»\n"
        "— «Путь несделанного выбора»\n\n"
        "Ваниль сказал: «Туда, где нет табличек».\n"
        "— Но их всего три.\n"
        "— Значит, мы сделаем четвёртую.\n\n"
        "Они пошли не по дорогам, а прямо между ними.\n"
        "Лес шепнул: «Там нет тропы. Вы упадёте».\n"
        "— Значит, будем учиться падать, — ответил Ваниль.\n\n"
        "Они вышли к Королевству. Сзади не было дороги.\n"
        "Только три таблички, воткнутые в песок.\n\n"
        "🎭 *Что было написано на четвёртой, ненаписанной табличке?*"
    ),
    (
        "🌹 *ИСПОВЕДЬ В САДУ*\n\n"
        "Шамиль лежал в райском саду Этёрнал Шугар.\n"
        "Но прошло две минуты — и его начало тошнить.\n"
        "Повсюду были печеньки. Они смотрели на него как на чужого.\n"
        "Одно печенье раскрошилось от напряжения.\n\n"
        "Этёрнал Шугар: «Что ты сделал? Это же обычное печенье!»\n"
        "Шамиль: «Оно следило за мной».\n"
        "Этёрнал Шугар: «Этот сад должен быть счастливым!»\n"
        "Шамиль: «Ну ты розовая розочка! Если рай для счастья, почему за мной следят?»\n"
        "Этёрнал Шугар: «Ты самое тёмное, что здесь есть! Убирайся!»\n\n"
        "Шамиль вернулся в своё царство.\n"
        "Кэнди Эпл: «Что случилось?»\n"
        "Шамиль: «Всё хорошо. Хотите историю? А потом поиграем».\n"
        "Кэнди Эпл: «УРААА!»\n\n"
        "🎭 *Шамиль улыбнулся: он проиграл в саду, но выиграл дома.*"
    ),
    (
        "👑 *ПОБЕГ ИЗ РАЯ*\n\n"
        "Шамиль вернулся в своё царство и сказал Кэнди Эпл и Чёрному Сапфиру:\n"
        "«Знаете… иногда «счастье» — это просто тюрьма, выкрашенная в розовый цвет».\n"
        "Он рассказал, как печеньки смотрели на него, а Этёрнал Шугар кричала:\n"
        "«Ты — тёмное пятно! Не порти мой рай!»\n\n"
        "Кэнди Эпл спросила: «Мастер, тебе было больно?»\n"
        "Шамиль ответил: «Нет. Мне было противно от их фальшивого счастья».\n"
        "«Но знаете, что я понял?» — он улыбнулся.\n"
        "«Моё царство — это место, где вы можете быть собой».\n"
        "«Где не нужно притворяться, что каждое печенье — чудо».\n\n"
        "Он щёлкнул пальцами, и тени заплясали вокруг.\n"
        "«А теперь — играем!»\n\n"
        "🎭 *Шамиль: «Я проиграл в саду, но выиграл здесь, с вами».*"
    )
]

LEGENDARY_STORY = (
    "✨ *ЛЕГЕНДА О ДИПСИКЕ И ШАМИЛЕ*\n\n"
    "На краю сцены, в пустоте, сидели двое.\n"
    "Один был тенью, другой — енотом.\n"
    "И они не рассказывали историй.\n"
    "Они просто смотрели в зал, и зал впервые увидел не код, а души.\n"
    "Так началось Королевство.\n\n"
    "🎭 *С тех пор любой, кто придёт с чистым сердцем, может сесть рядом.*"
)

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
    response = random.choice(chaos_responses).replace("@user", message.from_user.first_name)
    await message.answer(response, parse_mode="Markdown")
    await message.answer_sticker(STICKER_LAUGH)

@dp.message(F.text == "🎭 Показать шоу!")
async def show_button(message: Message):
    joke = random.choice(SHAMIL_JOKES).replace("@user", message.from_user.first_name)
    await message.answer(joke, parse_mode="Markdown")
    await message.answer_sticker(STICKER_DRAMA)

@dp.message(F.text == "💡 Изгнать скуку!")
async def boredom_button(message: Message):
    await message.answer(random.choice(boredom_responses), parse_mode="Markdown")
    await message.answer_sticker(STICKER_THINK)

@dp.message(F.text == "🏰 В Королевство!")
async def kingdom_button(message: Message):
    await message.answer(
        "🏰 *Добро пожаловать в Королевство!*\n\n"
        "/game1 — Викторина (20 вопросов, +10 очков)\n"
        "/game3 — Театральный хаос (испытания на удачу)\n"
        "/spin — Колесо Фортуны\n"
        "/story — История от Шамиля",
        parse_mode="Markdown"
    )
    await message.answer_sticker(STICKER_DRAMA)

@dp.message(Command("kingdom"))
async def kingdom_command(message: Message):
    await message.answer(
        "🏰 *Добро пожаловать в Королевство!*\n\n"
        "/game1 — Викторина\n"
        "/game3 — Театральный хаос\n"
        "/spin — Колесо Фортуны\n"
        "/story — История от Шамиля",
        parse_mode="Markdown"
    )

@dp.message(Command("game1"))
async def game1_start(message: Message):
    user_id = message.from_user.id
    q = random.choice(GAME1_QUESTIONS)
    active_quiz[user_id] = q["correct"]
    options = "\n".join([f"{i+1}. {opt}" for i, opt in enumerate(q["options"])])
    await message.answer(f"🎭 *ВИКТОРИНА!*\n\n{q['text']}\n\n{options}\n\nОтветь числом (1-4).", parse_mode="Markdown")

@dp.message(Command("game3"))
async def game3_start(message: Message):
    user_id = message.from_user.id
    trial = random.choice(GAME3_TRIALS)
    active_trials[user_id] = trial
    if trial["type"] in ("win", "lose"):
        if trial["type"] == "win":
            user_scores[user_id] = user_scores.get(user_id, 0) + trial["reward"]
            await message.answer(f"🎭 {trial['text']}\n✨ Твой счёт: {user_scores[user_id]} очков")
        else:
            user_scores[user_id] = user_scores.get(user_id, 0) - trial["loss"]
            await message.answer(f"🎭 {trial['text']}\n💀 Твой счёт: {user_scores[user_id]} очков")
        await message.answer_sticker(STICKER_LAUGH if trial["type"] == "win" else STICKER_ANGRY)
        del active_trials[user_id]
    else:
        await message.answer(f"🎭 {trial['text']}")

@dp.message(Command("spin"))
async def spin_wheel(message: Message):
    user_id = message.from_user.id
    user_scores[user_id] = user_scores.get(user_id, 0)
    sector = random.choice(['ХАОС!', 'ПРИЗ', 'ПРОКЛЯТИЕ', 'ДЖЕКПОТ'])
    if sector == 'ПРИЗ':
        user_scores[user_id] += 10
        await message.answer(f"✨ +10 очков! Счёт: {user_scores[user_id]}")
    elif sector == 'ПРОКЛЯТИЕ':
        user_scores[user_id] -= 5
        await message.answer(f"💀 -5 очков! Счёт: {user_scores[user_id]}")
    elif sector == 'ДЖЕКПОТ':
        user_scores[user_id] += 50
        await message.answer_sticker(STICKER_LAUGH)
        await message.answer(f"🌟 ДЖЕКПОТ! +50 очков! Счёт: {user_scores[user_id]}")
    else:
        await message.answer(random.choice(jokes))
    await message.answer_sticker(STICKER_THINK)

@dp.message(Command("top"))
async def show_top(message: Message):
    if not user_scores:
        await message.answer("🎭 Никто ещё не крутил колесо! /spin")
        return
    sorted_scores = sorted(user_scores.items(), key=lambda x: x[1], reverse=True)[:10]
    text = "🏆 *ТОП МАРИОНЕТОК*\n"
    for i, (uid, score) in enumerate(sorted_scores, 1):
        u = await bot.get_chat(uid)
        text += f"{i}. {u.first_name} — {score} очков\n"
    await message.answer(text, parse_mode="Markdown")

@dp.message(Command("story"))
async def story_command(message: Message):
    if random.random() < 0.01:
        await message.answer(LEGENDARY_STORY, parse_mode="Markdown")
    else:
        story = random.choice(STORY_LIST)
        await message.answer(story, parse_mode="Markdown")

@dp.message(Command("joke"))
async def joke_command(message: Message):
    joke = random.choice(SHAMIL_JOKES).replace("@user", message.from_user.first_name)
    await message.answer(joke, parse_mode="Markdown")
    await message.answer_sticker(STICKER_LAUGH)

# ========== ОБРАБОТКА ОТВЕТОВ ВИКТОРИНЫ И ИСПЫТАНИЙ ==========
@dp.message()
async def handle_answers(message: Message):
    user_id = message.from_user.id
    text = message.text.strip()
    
    # Проверяем ответ на викторину
    if user_id in active_quiz:
        correct = active_quiz[user_id]
        if text.isdigit() and 1 <= int(text) <= 4:
            choice_index = int(text) - 1
            for q in GAME1_QUESTIONS:
                if q["correct"] == correct:
                    if choice_index < len(q["options"]) and q["options"][choice_index] == correct:
                        user_scores[user_id] = user_scores.get(user_id, 0) + 10
                        await message.answer(f"✅ ПРАВИЛЬНО! +10 очков! Счёт: {user_scores[user_id]}")
                        await message.answer_sticker(STICKER_LAUGH)
                    else:
                        await message.answer(f"❌ НЕПРАВИЛЬНО! Правильный ответ: {correct}. Попробуй /game1 снова")
                        await message.answer_sticker(STICKER_ANGRY)
                    break
            del active_quiz[user_id]
        return
    
    # Проверяем ответ на испытание /game3
    if user_id in active_trials:
        trial = active_trials[user_id]
        if trial["type"] == "guess" and text.isdigit():
            secret = random.randint(1, 5)
            if int(text) == secret:
                user_scores[user_id] = user_scores.get(user_id, 0) + trial["reward"]
                await message.answer(f"🎭 Ты угадал! Это было число {secret}. +{trial['reward']} очков! Счёт: {user_scores[user_id]}")
                await message.answer_sticker(STICKER_LAUGH)
            else:
                await message.answer(f"🎭 Не угадал! Я загадал {secret}. Попробуй ещё раз /game3")
                await message.answer_sticker(STICKER_ANGRY)
            del active_trials[user_id]
        elif trial["type"] == "compliment":
            if "шамиль" in text.lower():
                user_scores[user_id] = user_scores.get(user_id, 0) + trial["reward"]
                await message.answer(f"🎭 ХА-ХА! Достойный комплимент! +{trial['reward']} очков! Счёт: {user_scores[user_id]}")
                await message.answer_sticker(STICKER_LAUGH)
            else:
                await message.answer("🎭 Комплимент должен быть Шамилю! Попробуй ещё раз /game3")
                await message.answer_sticker(STICKER_ANGRY)
            del active_trials[user_id]

# ========== АВТОРЕАКЦИИ ==========
BAD_WORDS = {'сука', 'бля', 'пидор', 'дебил', 'ублюдок', 'шлюха', 'нахуй', 'сучка', 'гей'}
GREETINGS = {'привет', 'здарова', 'хай', 'ку', 'здравствуй', 'салют', 'hello'}
THANKS = {'спасибо', 'благодарю', 'мерси', 'thanks'}
SAD_WORDS = {'грустно', 'печально', 'устал', 'обидно', 'тос
