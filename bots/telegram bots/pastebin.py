import telebot
import requests
bot = telebot.TeleBot('TOKEN')

expiries = ['N', "10M", "1H", "1D", "1W", "2W", "1M", "6M", "1Y"]
def title(message):
    title = message.text
    reply = f"""
Paste Name: {title}
Send your paste expiry.
9 Valid Options:
N = Never
10M = 10 Minutes
1H = 1 Hour
1D = 1 Day
1W = 1 Week
2W = 2 Weeks
1M = 1 Month
6M = 6 Months
1Y = 1 Year"""
    msg = bot.reply_to(message, reply)
    bot.register_next_step_handler(msg, expire, title)

def expire(message, title):
    title = title
    expiry = message.text
    if expiry not in expiries:
        reply = f"""
Paste Name: {title}
Expiry: {expiry}

Send your paste text."""
        expiry = "N"
        msg = bot.reply_to(message, reply)
        bot.register_next_step_handler(msg, text, title, expiry)
    else:
        reply = f"""
Paste Name: {title}
Expiry: {expiry}

Send your paste text."""
        msg = bot.reply_to(message,reply)
        bot.register_next_step_handler(msg, text, title, expiry)

def text(message, title, expire):
    chat_id = message.chat.id
    text = message.text
    title = title
    expiry = expire
    bot.send_message(chat_id, "Generating Pastebin URL...")
    key = 'KEY' # ur key
    login_data = {
    'api_dev_key': key,
    'api_user_name': 'USERNAME', # ur username
    'api_user_password': 'PASSWORD' # ur password
    }
    data = {
    'api_option': 'paste',
    'api_dev_key':key,
    'api_paste_code':text,
    'api_paste_expire_date': expiry,
    'api_paste_name':title,
    'api_user_key': None
    }
    login = requests.post("https://pastebin.com/api/api_login.php", data=login_data)
    r = requests.post("https://pastebin.com/api/api_post.php", data=data)
    if r.text == 'Bad API request, Post limit, maximum pastes per 24h reached' or 'Bad API request, Post limit, maximum pastes per 24h reached':
        bot.send_message(chat_id, f"Sorry maximum paste link have been reached. Please try again in 24 hrs.")
    else:
        reply = f"""
    URL Generated successfuly
    Paste Title: {title}
    Expiry: {expiry}
    Pastebin URL: {r.text}
    Generated By: @pastebinurl_bot"""
        bot.send_message(chat_id, reply)


@bot.message_handler(commands=['pb'])
def msg(message):
    msg = bot.reply_to(message, "Send your pastebin title.")
    bot.register_next_step_handler(msg, title)

@bot.message_handler(commands=['start'])
def msg(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,f"Hello {message.chat.first_name},\nI am Pastebin Bot that generates pastebin url from your text.\nTo start use - /pb\nMade By: @sudopao")
bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.infinity_polling()
