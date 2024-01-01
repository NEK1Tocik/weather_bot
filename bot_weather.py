import telebot
import requests
import json

bot = telebot.TeleBot('YOUR_BOT_TOKEN')
API = '3d9de74844d28377e81415151cbe6a66'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Приветствую, рад тебя видеть! Напиши название города')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
       data = json.loads(res.text) # преобразуем в формат json
       temp = data["main"]["temp"]
       bot.reply_to(message, f'Сейчас погода: {temp}')

       image = 'sunny.jpg' if temp > 6.0 else 'sun1.png'
       file = open('./' + image, 'rb')
       bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, 'Город указан не верно!')


bot.polling(none_stop=True)
