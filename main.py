#from faulthandler import disable
#from http import HTTPStatus
#from re import A
from config import TOKEN
import logging

from telegram import KeyboardButton, Location, ReplyKeyboardMarkup, Update, ParseMode  
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
)


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)


logger = logging.getLogger(__name__)


# Start - Main menu
def start(update: Updater, context: CallbackContext):
    reply_keyboard = [['Taomlar'], ['Ichimliklar'], ['Buyurtma berish'], ['Bizning manzil']]

    message = 'Assalom alaykum! Bizning restoranimiz  rasmiy telegram botiga xush kelibsiz!'
    photo = "Images/Restaurant.jpg"

    update.message.reply_photo(
        photo=open(photo, 'rb'), caption=message, parse_mode='HTML',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    )

 
def foods(update: Updater, context: CallbackContext):
    reply_keyboad = [['Quyuq taomlar'], ['Suyuq taomlar'], ['Saladlar'], ['Shirinliklar'], ['Ortga']]

    update.message.reply_html(
        'Restoranimizda turli tuman quyuq, suyuq taomlar, saladlar va shirinliklar mavjud',     
        reply_markup=ReplyKeyboardMarkup(reply_keyboad, one_time_keyboard=True, resize_keyboard=True)
    )


def drinks(update: Updater, context: CallbackContext):
    try:
        message1 = '<b>1. Ichimlik:</b> Qora choy\n<b>Narxi:</b> 10000 so\'m'
        photo1 = "Images/Black Tea.webp"
        update.message.reply_photo(
            photo=open(photo1, 'rb'), caption=message1, parse_mode='HTML'
        )
        message2 = '<b>2. Ichimlik:</b> Ko\'k choy\n<b>Narxi:</b> 10000 so\'m'
        photo2 = "Images/Green Tea.jpg"
        update.message.reply_photo(
            photo=open(photo2, 'rb'), caption=message2, parse_mode='HTML'
        )
        message3 = '<b>3. Ichimlik:</b> Americano\n<b>Narxi:</b> 17000 so\'m'
        photo3 = "Images/Americano.jpg"
        update.message.reply_photo(
            photo=open(photo3, 'rb'), caption=message3, parse_mode='HTML'
        )
        message4 = '<b>4. Ichimlik:</b> Latte\n<b>Narxi:</b> 22000 so\'m'
        photo4 = "Images/Latte.jpg"
        update.message.reply_photo(
            photo=open(photo4, 'rb'), caption=message4, parse_mode='HTML'
    )
    except Exception as e:
        print('Error', str(e))


def order(update: Updater, context: CallbackContext):
    update.message.reply_text(
        'Buyurtma berish uchun +16467052261  raqamiga bog\'laning yoki @shamsiddinabbosov ga murojaat qiling!'
    )


def address(update: Updater, context: CallbackContext):
    message = '32 Cedar street\nNew York | NY 10005\nNow only Available for Delivery and Takeout'
    photo = "Images/Address.jpg"
    update.message.reply_photo(
        photo=open(photo, 'rb'), caption=message, parse_mode='HTML'
    )


# Foods
def thick(update: Updater, context: CallbackContext):
    message1 = '<b>1. Quyuq taom:</b> Osh\n<b>Narxi:</b> 25000 so\'m'
    photo1 = "Images/Osh.jpg"
    update.message.reply_photo(
        photo=open(photo1, 'rb'), caption=message1, parse_mode='HTML'
    )
    message2 = '<b>2. Quyuq taom:</b> Qovurma lag\'mon\n<b>Narxi:</b> 26000 so\'m'
    photo2 = "Images/Qovurma lag'mon.jpg"
    update.message.reply_photo(
        photo=open(photo2, 'rb'), caption=message2, parse_mode='HTML'
    )
    message3 = '<b>3. Quyuq taom:</b> Qozon kabob\n<b>Narxi:</b> 38000 so\'m'
    photo3 = "Images/Qozon kabob.jpg"
    update.message.reply_photo(
        photo=open(photo3, 'rb'), caption=message3, parse_mode='HTML'
    )
    message4 = '<b>4. Quyuq taom:</b> Tovuqli Spagetti\n<b>Narxi:</b> 33000 so\'m'
    photo4 = "Images/Tovuqli Spagetti.jpg"
    update.message.reply_photo(
        photo=open(photo4, 'rb'), caption=message4, parse_mode='HTML'
    )


def liquid(update: Updater, context: CallbackContext):
    message1 = '<b>1. Suyuq taom:</b> Qaynatma sho\'rva\n<b>Narxi:</b> 28000 so\'m'
    photo1 = "Images/Qaynatma sho'rva.jpg"
    update.message.reply_photo(
        photo=open(photo1, 'rb'), caption=message1, parse_mode='HTML'
    )
    message2 = '<b>2. Suyuq taom:</b> Moshxo\'rda\n<b>Narxi:</b> 25000 so\'m'
    photo2 = "Images/Moshxo'rda.jpg"
    update.message.reply_photo(
        photo=open(photo2, 'rb'), caption=message2, parse_mode='HTML'
    )
    message3 = '<b>3. Suyuq taom:</b> Mastava\n<b>Narxi:</b> 25000 so\'m'
    photo3 = "Images/Mastava.jpg"
    update.message.reply_photo(
        photo=open(photo3, 'rb'), caption=message3, parse_mode='HTML'
    )
    message4 = '<b>4. Suyuq taom:</b> Chuchvara\n<b>Narxi:</b> 25000 so\'m'
    photo4 = "Images/Chuchvara.jpg"
    update.message.reply_photo(
        photo=open(photo4, 'rb'), caption=message4, parse_mode='HTML'
    )


def salad(update: Updater, context: CallbackContext):
    message1 = '<b>1. Salad:</b> Yunoncha\n<b>Narxi:</b> 26000 so\'m'
    photo1 = "Images/Yunoncha.jpg"
    update.message.reply_photo(
        photo=open(photo1, 'rb'), caption=message1, parse_mode='HTML'
    )
    message2 = '<b>2. Salad:</b> Olivier\n<b>Narxi:</b> 21000 so\'m'
    photo2 = "Images/Olivier.jpg"
    update.message.reply_photo(
        photo=open(photo2, 'rb'), caption=message2, parse_mode='HTML'
    )
    message3 = '<b>3. Salad:</b> Vinaigrette\n<b>Narxi:</b> 14000 so\'m'
    photo3 = "Images/Vinaigrette.jpg"
    update.message.reply_photo(
        photo=open(photo3, 'rb'), caption=message3, parse_mode='HTML'
    )
    message4 = '<b>4. Salad:</b> Bruklin\n<b>Narxi:</b> 60000 so\'m'
    photo4 = "Images/Bruklin.jpg"
    update.message.reply_photo(
        photo=open(photo4, 'rb'), caption=message4, parse_mode='HTML'
    )


def sweet(update: Updater, context: CallbackContext):
    message1 = '<b>1. Shirinlik:</b> Oreo keki\n<b>Narxi:</b> 31000 so\'m'
    photo1 = "Images/Oreo keki.jpg"
    update.message.reply_photo(
        photo=open(photo1, 'rb'), caption=message1, parse_mode='HTML'
    )
    message2 = '<b>2. Shirinlik:</b> Snickers\n<b>Narxi:</b> 40000 so\'m'
    photo2 = "Images/Snickers.jpg"
    update.message.reply_photo( 
        photo=open(photo2, 'rb'), caption=message2, parse_mode='HTML'
    )
    message3 = '<b>3. Shirinlik:</b> Truffle\n<b>Narxi:</b> 14000 so\'m'
    photo3 = "Images/Truffle.jpg"
    update.message.reply_photo(
        photo=open(photo3, 'rb'), caption=message3, parse_mode='HTML'
    )
    message4 = '<b>4. Shirinlik:</b> Limonli pirog\n<b>Narxi:</b> 27000 so\'m'
    photo4 = "Images/Limonli pirog.jpg"
    update.message.reply_photo(
        photo=open(photo4, 'rb'), caption=message4, parse_mode='HTML'
    )


def back(update: Updater, context: CallbackContext):
    reply_keyboard = [['Taomlar'], ['Ichimliklar'], ['Buyurtma berish'], ['Bizning manzil']]

    update.message.reply_html(
        'Agar bot yuzasidan takliflaringiz bo\'lsa, @shamsiddinabbosov\'ga murojaat qilishingiz mumkin',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    )


# Run
def main() -> None:
    """Run the bot."""
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.regex('^Taomlar$'), foods))
    dispatcher.add_handler(MessageHandler(Filters.regex('^Ichim liklar$'), drinks))
    dispatcher.add_handler(MessageHandler(Filters.regex('^Buyurtma berish$'), order))
    dispatcher.add_handler(MessageHandler(Filters.regex('^Bizning manzil$'), address))
    dispatcher.add_handler(MessageHandler(Filters.regex('^Quyuq taomlar$'), thick))
    dispatcher.add_handler(MessageHandler(Filters.regex('^Suyuq taomlar$'), liquid))
    dispatcher.add_handler(MessageHandler(Filters.regex('^Saladlar$'), salad))
    dispatcher.add_handler(MessageHandler(Filters.regex('^Shirinliklar$'), sweet))
    dispatcher.add_handler(MessageHandler(Filters.regex('^Ichimliklar$'), drinks))
    dispatcher.add_handler(MessageHandler(Filters.regex('^Ortga$'), back))


    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()