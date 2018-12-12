from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
import requests
from bs4 import BeautifulSoup
import urllib3
import random
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
import datetime
datetime.datetime.now()
import json
import os
def start(bot, update):
  i = random.randint(0,1)
  if i == 1:
      update.message.reply_text("Утро недоброе!")
  else:
      update.message.reply_text("Не ждали?!")

def dem(bot, update):
    try:
        params = {'timeout': 100, 'offset': None}
        res = requests.get("http://demotivation.me/", timeout)
        html_page = res.content
        soup = BeautifulSoup(html_page, 'html.parser')
        b = soup.findAll("a")
        h=b[4].findAll("img")[0]['src']
        update.message.reply_photo("http://demotivation.me" +"/images" + h[7:len(h)])
    except Exception as e:
        print("Exception (find):", e)
    pass
def vity(bot, update):
  if update.message.date.date() != datetime.datetime.now().date():
    return
  text = update.message.text.lower()
  answer = "";
  if "надо" in text:
      answer += " Нам это не надо!"
  if "знаю" in text:
      answer +=" Я знаю то, чего знаю!"
  if "плюн" in text:
      answer +=" Тьфу бля!"
  if "вод" in text:
      answer +=" Воды-то нету!"
  if "исходники" in text:
      answer +=" Я не умею использовать гит, но мои исходники лежат тут: https://github.com/mksmbrtsh/vity"
  if "чаю" in text or "чай" in text:
      i = random.randint(0,1)
      if i == 1:
          answer +=" Всю воду выпили, сосуны!"
      else:
          answer +="*молча паяет чайник*"
  if "програм" in text:
      answer +=" Конечно, я тут больше всех программирую!"
  if "окно" in text or "проветри" in text:
      answer +=" Мужчина, окно закрой!"
  if "не дума" in text:
      answer +=" *удаляет терминал из администратора*"
  if "10" in text or "десять" in text:
      answer +=" Ваша виндос - говно!"
  if "вит" in text or "вик" in text:
      i = random.randint(0,1)
      if i == 1:
          answer +=" Мы с тобой не наравных!"
      else:
          answer +=" Ты оборзел!"
  if "тест" in text:
      answer += " Тебе надо поиспражняться."
  if "морф" in text:
      
      t = text[text.index("морф",0, len(text)) + 5: len(text)]
      c = t.split(" ")
      for s in c:
        w = morph.parse(s)[0]
        v1 = w.normal_form 
        answer +=  v1 +" "
  if "не работа" in text:
      i = random.randint(0,6)
      if i == 0:
         answer += " Лежит, есть не просит..."
      elif i == 1:
         answer += " Ну голупшик, испортили базу." 
      elif i == 2:
         answer += " Я так и не соображу из-за чего. "
      elif i == 3:
         answer += " Что-то ты такое там видимо напорол, вот и всё."
      elif i == 4:
         answer += " Учи матчасть!"
      elif i == 5:
         answer += " Перепаяй конденцаторы!"
      elif i == 6:
         answer += " Во всём виноват Вадим"
  if "сделать" in text:
      answer += " Голубчик, я домой ухожу."
  if "сет" in text:
      answer +=" Я тридцать лет программирую сети!"
  if "интернет" in text:
      answer +=" Я вы знаете, у меня дома нет интернета!"
  if "помн" in text or "забы" in text:
      answer +=" Я всё помню, мужчина, это ты ничего не помнишь или забыл!"
  if "ровн" in text:
      answer +=" Мы с тобой не наравных!"
  if len(answer) > 1 and "погод" not in text:
      update.message.reply_text(answer[1:len(answer)])
  if "дем" in text:
      try:
            params = {'timeout': 100, 'offset': None}
            res = requests.get("http://demotivation.me/", params)
            html_page = res.content
            soup = BeautifulSoup(html_page)
            b = soup.findAll("img")
            i = random.randint(0,36)
            h=b[i]['src']
            update.message.reply_photo("http://demotivation.me" +"/images" + h[7:len(h)])
      except Exception as e:
        print("Exception (find):", e)
      pass
  if "курс" in text:
      try:
        params = {'timeout': 100, 'offset': None}
        res = requests.get("https://www.sberbank.ru/portalserver/proxy/?pipe=shortCachePipe&url=http%3A%2F%2Flocalhost%2Frates-web%2FrateService%2Frate%2Fcurrent%3FregionId%3D77%26rateCategory%3Dbase%26currencyCode%3D840", params)
        j = json.loads(res.text)
        update.message.reply_text("Про доллар. На сайте у грефа показывается(0-999$):\nпокупка " + str(j["base"]["840"]["0"]["buyValuePrev"]) +", продажа " + str(j["base"]["840"]["0"]["sellValuePrev"]) + "\nПо факту греф сейчас делает(0-999$):\nпокупка " + str(j["base"]["840"]["0"]["buyValue"]) + ", продажа " + str(j["base"]["840"]["0"]["sellValue"]))
      except Exception as e:
        print("Exception (find):", e)
      pass
  if "погод" in text:
    s_city= ""
    s_city1 = ""
    c = ""
    if "павловская слобода" in text or "слобода" in text or "павловской слободе" in text or "слободе" in text or "дыре" in text:
        s_city =  "павловская слобода"
        s_city1 =  "павловская слобода"
    else:
        t = text[text.index("погод",0, len(text)): len(text)]
        c = t.split(" ")
        if(len(c) ==1):
            s_city = "Moscow,RU"
        elif len(c) == 2:
            s_city = c[1]
        elif len(c) >= 3 and len(c[1]) == 1:
            s_city = t[ 9: len(text)]
        else:
            s_city = t[ 7: len(text)]
        cc = s_city.split(" ")
        
        for s in cc:
            w = morph.parse(s)[0]
            v1 = w.normal_form 
            s_city1 += v1 +" "
        if s_city1[len(s_city1)-1] == ' ':
            s_city1 = s_city1[0: len(s_city1)-1]
    appid = "805f4a6eb937d5eada7f94f42b798a03"
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find", params={'q': s_city1, 'type': 'like', 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        if len(c) ==1:
          s_city = "Москве"
        if len(answer) >1:
          answer += " Но"
        elif len(data['list']) == 0:
          answer +=" Витя не знает такой городишко: " + s_city1
        elif s_city == "павловская слобода":
            answer +=" В центре мира Павловской Слободе сейчас " + (data['list'][0]['weather'][0]['description'] + " " + str(data['list'][0]['main']['temp']) +"°C, ветер: " + str(data['list'][0]['wind']['speed']) +", влажность: " + str(data['list'][0]['main']['humidity']) + "%, давление: " + str(round(data['list'][0]['main']['pressure'] / 1.333224, 2)) + "мм р.ст." )
        else:
            answer +=" " + (data['list'][0]['weather'][0]['description'] + " в " + s_city + " " + str(data['list'][0]['main']['temp']) +"°C, ветер: " + str(data['list'][0]['wind']['speed']) +", влажность: " + str(data['list'][0]['main']['humidity']) + "%, давление: " + str(round(data['list'][0]['main']['pressure'] / 1.333224, 2)) + "мм р.ст." )
        update.message.reply_text(answer[1:len(answer)])
    except Exception as e:
        print("Exception (find):", e)
    pass
def main():
  # Create Updater object and attach dispatcher to it
  PORT = int(os.environ.get('PORT', '8443'))
  updater = Updater('764873983:AAH3IHus1g6kQCkmqaApTBfFZbvCEoOe-wo')
  updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path='764873983:AAH3IHus1g6kQCkmqaApTBfFZbvCEoOe-wo')
  updater.bot.set_webhook("https://floating-castle-58368.herokuapp.com/764873983:AAH3IHus1g6kQCkmqaApTBfFZbvCEoOe-wo")
  dispatcher = updater.dispatcher
  print("Bot started")
  # Add command handler to dispatcher
  start_handler = CommandHandler('start',start)
  dispatcher.add_handler(start_handler)
  dem_handler = CommandHandler('dem',dem)
  dispatcher.add_handler(dem_handler)
  vity_handler = MessageHandler(Filters.text,vity)
  dispatcher.add_handler(vity_handler)
  # Start the bot
  updater.start_polling()

  # Run the bot until you press Ctrl-C
  updater.idle()

if __name__ == '__main__':
  main()