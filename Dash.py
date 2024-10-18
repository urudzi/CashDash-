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
        [InlineKeyboardButton("Главное меню", callback_data='main_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привет! Я бот CashDASH, я помогу тебе заработать", reply_markup=reply_markup)

# Главное меню с выбором кнопок
async def main_menu(update: Update, context):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("Получить уникальную ссылку для регистрации", callback_data='registration')],
        [InlineKeyboardButton("Получить уникальный промокод", callback_data='promo')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="Выбери одно из действий:", reply_markup=reply_markup)

# Обработка нажатий кнопок
async def button(update: Update, context):
    query = update.callback_query
    await query.answer()

    if query.data == 'main_menu':
        await main_menu(update, context)

    elif query.data == 'registration':
        # Описание и кнопка
        await query.edit_message_text(text=f"Уникальная ссылка даст тебе доступ к эксклюзивным бонусам казино. Нажми на кнопку ниже, чтобы получить свою ссылку.\n\n"
                                           f"Получить: {registration_link}")

    elif query.data == 'promo':
        # Анимация генерации промокода
        await query.edit_message_text(text="Твой промокод позволит тебе активировать бонусы при регистрации. Идет генерация... [0%[||||...............]100%]")
        
        loading_time = random.randint(7, 15)  # Случайное время между 7 и 15 секундами
        progress_bar_length = 10  # Длина прогресс-бара

        for i in range(1, 101, 10):
            progress_bar = '|' * (i // 10) + '.' * (progress_bar_length - (i // 10))
            await query.edit_message_text(text=f"Идет генерация... [{i}%[{progress_bar}]100%")
            time.sleep(loading_time / 10)  # Разделяем общее время на 10 шагов

        promo_code = random.choice(promo_codes)  # Случайно выбираем промокод
        await query.edit_message_text(text=f"Твой уникальный промокод: {promo_code}")

# Основная функция запуска бота
def main():
    application = ApplicationBuilder().token("YOUR_TELEGRAM_BOT_TOKEN").build()

    # Обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    # Запуск бота с использованием polling
    application.run_polling()

# Запуск программы
if __name__ == '__main__':
    main()