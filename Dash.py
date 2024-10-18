import random
import time
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

# Список промокодов
promo_codes = ['THXY', '10X0', 'SXXS']

# Уникальная ссылка для регистрации
registration_link = "https://1warlo.top/casino/list?open=register&p=7paw"

# Функция для старта бота и приветствия
async def start(update: Update, context):
    # Проверяем, пришло ли сообщение как результат команды или через callback
    if update.message:
        # Если сообщение пришло через команду
        chat_id = update.message.chat_id
        keyboard = [
            [InlineKeyboardButton("🔗 Ссылка на регистрацию", callback_data='registration_menu')],
            [InlineKeyboardButton("🎁 Генерация промокода", callback_data='promo_menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("💰 Привет! Я бот CashDASH🤖. Я помогу тебе заработать! Спросишь как❓Так все просто👌🏻, у меня есть возможность генерации промокода для 1win💠, который даст тебе возможность не только приумножить свой депозит в 5 РАЗ🤑, так и повысит твой шанс на успех💯, а по моей ссылки на регистрацию у тебя всегда будет жирный ➕‼️Не жди, а зарабатывай со мной💸", reply_markup=reply_markup)
    elif update.callback_query:
        # Если сообщение пришло через нажатие кнопки
        query = update.callback_query
        keyboard = [
            [InlineKeyboardButton("🔗 Ссылка на регистрацию", callback_data='registration_menu')],
            [InlineKeyboardButton("🎁 Генерация промокода", callback_data='promo_menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="💰 Привет! Я бот CashDASH. Я помогу тебе заработать! 💸", reply_markup=reply_markup)

# Меню для ссылки на регистрацию
async def registration_menu(update: Update, context):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("🚀 Получить", callback_data='registration')],
        [InlineKeyboardButton("🏠 Главное меню", callback_data='main_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="🔗 Получи свою уникальную ссылку на регистрацию и начни зарабатывать! 💸", reply_markup=reply_markup)

# Меню для генерации промокодов
async def promo_menu(update: Update, context):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("🎲 Сгенерировать", callback_data='promo')],
        [InlineKeyboardButton("🏠 Главное меню", callback_data='main_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="🎁 Я сгенерирую тебе уникальный промокод на +500% к пополнению. Готов? 💥", reply_markup=reply_markup)

# Обработка нажатий кнопок
async def button(update: Update, context):
    query = update.callback_query
    await query.answer()

    if query.data == 'main_menu':
        await start(update, context)

    elif query.data == 'registration_menu':
        await registration_menu(update, context)

    elif query.data == 'promo_menu':
        await promo_menu(update, context)

    elif query.data == 'registration':
        # Описание и кнопка
        keyboard = [[InlineKeyboardButton("🏠 Главное меню", callback_data='main_menu')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=f"🔗 Твоя уникальная ссылка для регистрации: [{registration_link}](https://{registration_link})", reply_markup=reply_markup, parse_mode="Markdown")

    elif query.data == 'promo':
        # Анимация генерации промокода с случайными шагами
        await query.edit_message_text(text="🎲 Идет генерация... 0%")
        
        loading_time = random.randint(7, 15)  # Случайное время между 7 и 15 секундами
        current_progress = 0  # Текущий прогресс
        progress_bar_length = 10  # Длина прогресс-бара

        while current_progress < 100:
            step = random.randint(1, 20)  # Случайный шаг от 1% до 20%
            current_progress = min(current_progress + step, 100)  # Обновляем прогресс, но не больше 100%
            progress_bar = '|' * (current_progress // 10) + '.' * (progress_bar_length - (current_progress // 10))
            await query.edit_message_text(text=f"🎲 Идет генерация... {current_progress}% {progress_bar}")
            time.sleep(loading_time / 10)  # Задержка между обновлениями

        promo_code = random.choice(promo_codes)  # Случайно выбираем промокод
        keyboard = [[InlineKeyboardButton("🏠 Главное меню", callback_data='main_menu')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=f"🎁 Твой уникальный промокод: [{promo_code}](https://t.me/share/url?url={promo_code})", reply_markup=reply_markup, parse_mode="Markdown")

# Основная функция запуска бота
def main():
    application = ApplicationBuilder().token("7836847076:AAHVcgjHmMErXbyUIcqt__PpceYyHfraoi8").build()

    # Обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    # Запуск бота с использованием polling
    application.run_polling()

# Запуск программы
if __name__ == '__main__':
    main()