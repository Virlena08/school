import logging
from telegram.ext import Application, MessageHandler, filters
from telegram import ReplyKeyboardMarkup
from telegram.ext import Application
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardRemove
from config import BOT_TOKEN

logger = logging.getLogger(__name__)

# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
reply_keyboard = [['/address'],
                  ['/phone'],
                  ['/site'],
                  ['/work_time']]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

async def start(update, context):
    """Отправляет сообщение когда получена команда /start"""
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет {user.mention_html()}! Я План-бот. Я помогу отслеживать процесс выполнения задач!",
    )


async def help_command(update, context):
    """Отправляет сообщение когда получена команда /help"""
    await update.message.reply_text("Здесь перечень всех команд, на которые я откликаюсь.\
                                    /create - создание новой цели(задачи)\
                                    /delete - удаление существующей цели(задачи)" )

async def address(update, context):
    await update.message.reply_text(
        "Адрес: г. Москва, ул. Льва Толстого, 16")


async def phone(update, context):
    await update.message.reply_text("Телефон: +7(495)776-3030")


async def site(update, context):
    await update.message.reply_text(
        "Сайт: http://www.yandex.ru/company")


async def work_time(update, context):
    await update.message.reply_text(
        "Время работы: круглосуточно.")





# Зарегистрируем их в приложении перед
# регистрацией обработчика текстовых сообщений.
# Первым параметром конструктора CommandHandler я
# вляется название команды.



def main():
    # Создаём объект Application.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
    application = Application.builder().token(BOT_TOKEN).build()

    # Создаём обработчик сообщений типа filters.TEXT
    # из описанной выше асинхронной функции echo()
    # После регистрации обработчика в приложении
    # эта асинхронная функция будет вызываться при получении сообщения
    # с типом "текст", т. е. текстовых сообщений.
    application.add_handler(CommandHandler("address", address))
    application.add_handler(CommandHandler("phone", phone))
    application.add_handler(CommandHandler("site", site))
    application.add_handler(CommandHandler("work_time", work_time))
    # Регистрируем обработчик в приложении.
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Запускаем приложение.
    application.run_polling()
# Зарегистрируем их в приложении перед
# регистрацией обработчика текстовых сообщений.
# Первым параметром конструктора CommandHandler я
# вляется название команды.


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
