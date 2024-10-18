import random
import time
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

# Список промокодов
promo_codes = ['THXY', '10X0', 'SXXS']  # Добавь сюда свои промокоды

# Уникальная ссылка для регистрации
registration_link = "https://1warlo.top/casino/list?open=register&p=7paw"

# Функция для старта бота и приветствия
async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Ссылка на регистрацию", callback_data='registration_menu')],
        [InlineKeyboardButton("Генерация промокода", callback_data='promo_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привет! Я бот CashDASH, я помогу тебе заработать", reply_markup=reply_markup)

# Главное меню
async def main_menu(update: Update, context):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("Ссылка на регистрацию", callback_data='registration_menu')],
        [InlineKeyboardButton("Генерация промокода", callback_data='promo_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="Привет! Я бот CashDASH, я помогу тебе заработать", reply_markup=reply_markup)

# Меню для ссылки на регистрацию
async def registration_menu(update: Update, context):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("Получить", callback_data='registration')],
        [InlineKeyboardButton("Главное меню", callback_data='main_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="Получи свою уникальную ссылку на регистрацию", reply_markup=reply_markup)

# Меню для генерации промокодов
async def promo_menu(update: Update, context):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("Сгенерировать", callback_data='promo')],
        [InlineKeyboardButton("Главное меню", callback_data='main_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="Я сгенерирую тебе уникальный промокод на +500% к пополнению", reply_markup=reply_markup)

# Обработка нажатий кнопок
async def button(update: Update, context):
    query = update.callback_query
    await query.answer()

    if query.data == 'main_menu':
        await main_menu(update, context)

    elif query.data == 'registration_menu':
        await registration_menu(update, context)

    elif query.data == 'promo_menu':
        await promo_menu(update, context)

    elif query.data == 'registration':
        # Описание и кнопка
        keyboard = [[InlineKeyboardButton("Главное меню", callback_data='main_menu')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=f"Твоя уникальная ссылка для регистрации: [{registration_link}](https://{registration_link})", reply_markup=reply_markup, parse_mode="Markdown")

    elif query.data == 'promo':
        # Анимация генерации промокода
        await query.edit_message_text(text="Идет генерация... 0%")

        loading_time = random.randint(7, 15)  # Случайное время между 7 и 15 секундами
        progress_bar_length = 10  # Длина прогресс-бара

        for i in range(1, 101, 1):  # Шаг в 1%
            progress_bar = '|' * (i // 10) + '.' * (progress_bar_length - (i // 10))
            await query.edit_message_text(text=f"Идет генерация... {i}% {progress_bar}")
            time.sleep(loading_time / 100)  # Разделяем время на 100 шагов

        promo_code = random.choice(promo_codes)  # Случайно выбираем промокод
        keyboard = [[InlineKeyboardButton("Главное меню", callback_data='main_menu')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=f"Твой уникальный промокод: [{promo_code}](https://t.me/share/url?url={promo_code})", reply_markup=reply_markup, parse_mode="Markdown")

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