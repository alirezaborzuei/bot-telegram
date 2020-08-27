#!/usr/bin/env python
# -*- coding: utf-8 -*
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from boom.create import createporduct
updater = Updater("1080958406:AAEjfkoV019XFaDgwnA-9ri89FnBfGphwrE", use_context=True)


def error(update, context):
    """Log Errors caused by Updates."""
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def welcome(update, context):
     chat_id = update.effective_chat.id
     context.bot.sendMessage(chat_id, text="سلام.به ربات پیشنهاد محصول خوش آمدید.")


def menu(update, context):
    welcome(update, context)
    keyboard = [[InlineKeyboardButton("منوی محصولات", callback_data='product_menu'),
                 InlineKeyboardButton("منوی پیشنهادات ", callback_data='recommend_menu')],
                ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(text="لطفا منوی مورد نظر را انتخاب نمائید:", reply_markup=reply_markup)


def product_menu(update, context):
    query = update.callback_query
    keyboard = [[InlineKeyboardButton("ایجاد", callback_data='create_product'),
                 InlineKeyboardButton("حذف ", callback_data='del')],
                [InlineKeyboardButton("ویرایش", callback_data='edit'),
                 InlineKeyboardButton("جستجو", callback_data='search'),
                 InlineKeyboardButton("نظر سنجی", callback_data='comment')],
                [InlineKeyboardButton("بازگشت", callback_data='menu')]
                ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text('لطفا عملیات محصول خود انتخاب نمائید:', reply_markup=reply_markup)


def recommend_menu(update, context):
    query = update.callback_query
    query.edit_message_text(text="منوی شما: {}".format(query.data))


if __name__ == '__main__':
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', menu))
    dp.add_handler(CallbackQueryHandler(product_menu, pattern='product_menu'))
    dp.add_handler(CallbackQueryHandler(recommend_menu, pattern='recommend_menu'))
    dp.add_handler(CallbackQueryHandler(createporduct(dp), pattern='create_product'))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()
