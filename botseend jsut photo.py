
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, CallbackQueryHandler)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
updater = Updater("1080958406:AAEjfkoV019XFaDgwnA-9ri89FnBfGphwrE", use_context=True)

def add(update,context):
    keyboard = [[InlineKeyboardButton("1\u2B50", callback_data='1'),
                 InlineKeyboardButton("2\u2B50 ", callback_data='2')],
                [InlineKeyboardButton("3\u2B50", callback_data='3'),
                  InlineKeyboardButton("4\u2B50 ", callback_data='4'),
                 InlineKeyboardButton("5\u2B50", callback_data='5'),
                ]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    context.bot.send_photo(chat_id=update.message.chat_id, photo=open(r'./image/688193.jpg', 'rb')
                           , caption="this is 232323", reply_markup=reply_markup)



if __name__ == '__main__':
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', add))
    updater.start_polling()
    updater.idle()
