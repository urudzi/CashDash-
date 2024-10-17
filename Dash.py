import random
import time
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

# Список промокодов, которые бот будет случайно выдавать
promo_codes = ['THXY', '10X0', 'SXXS']  # Добавь сюда свои промокоды

# Уникальная ссылка для регистрации
registration_link = "https://1warlo.top/casino/list?open=register&p=7paw"

# Функция для старта бота и приветствия
async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Получить уникальную ссылку для регистрации", callback_data='registration')],
        [InlineKeyboardButton("Сгенерировать уникальный промокод", callback_data='promo')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привет! Выбери одно из действий:", reply_markup=reply_markup)

# Обработка нажатий кнопок
async def button(update: Update, context):
    query = update.callback_query
    await query.answer()

    if query.data == 'registration':
        # Отправляем уникальную ссылку
        await query.edit_message_text(text=f"Твоя уникальная ссылка для регистрации: {registration_link}")

    elif query.data == 'promo':
        # Генерация промокода с анимацией
        await query.edit_message_text(text="Идет генерация... [0%]")
        for i in range(1, 101, 10):
            time.sleep(0.5)  # Имитируем задержку для "анимации"
            await query.edit_message_text(text=f"Идет генерация... [{i}%]")
        promo_code = random.choice(promo_codes)  # Случайно выбираем промокод
        await query.edit_message_text(text=f"Твой уникальный промокод: {promo_code}")

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